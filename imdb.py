__author__ = 'zhenbangxiao'

'''
imdb is a command line interface program for searching movies, actors, directors in the Internet Movie Database.
'''

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import sys

version = '0.0.0.1'
urlPrefix = 'http://m.imdb.com/'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'
titleSearch = 'title/'
nameSearch = 'name/'
examplePage = open ('example.html', 'w')


def main ():
    if len (sys.argv) == 1 or sys.argv[1] == '--help':
        print ('\nimdb ' + version)
        ## Help messages
        print ('A command line interface program for searching movies, actors, directors in the Internet Movie Database.')
        print ('Project GitHub: http://github.com/starkshaw/imdb')
        print ('\n    OPTIONS')
        print ('    --id [titleID/personID]\tSearch by movie ID or person ID.')
        print ('    --help\t\t\tPrint out the help message.')
        print ()
    elif sys.argv[1] == '--id' and len (sys.argv) >= 3 and (sys.argv[2][0:2] == 'tt' or sys.argv[2][0:2] == 'nm'):
        print ('\nimdb ' + version)
        print ('\nFinding movie ID ' + sys.argv[2] + '...\n') if sys.argv[2][0:2] == 'tt' else print ('Finding person ID ' + sys.argv[2] + '...\n')
        if sys.argv[2][0:2] == 'tt':
            url = urlPrefix + titleSearch + sys.argv[2]
            header = {'Connection': 'keep-alive', 'User-Agent': user_agent}
            request = Request (url, headers = header)
            response = urlopen (request)
            htmlStr = response.read ()
            rawPage = BeautifulSoup (htmlStr, "html.parser")
            examplePage.write (str (rawPage))
            examplePage.close ()
            # print (htmlStr)
            title = rawPage.head.title.string
            title = title[0:title.rfind ('-', 0, len (title))]
            print (title)
        elif sys.argv[2][0:2] == 'nm':
            url = urlPrefix + nameSearch + sys.argv[2]
            header = {'Connection': 'keep-alive', 'User-Agent': user_agent}
            request = Request (url, headers = header)
            response = urlopen (request)
            htmlStr = response.read ()
            rawPage = BeautifulSoup (htmlStr, "html.parser")
            examplePage.write (str (rawPage))
            examplePage.close ()
            title = rawPage.head.title.string
            title = title[0:title.rfind ('-', 0, len (title))]
            print (title)
    else:
        print ('\nInvalid parameter:') if len (sys.argv) == 2 else print ('\nInvalid parameters:')
        for i in range (1, len (sys.argv)):
            sys.stdout.write (sys.argv[i] + ' ')
        print ('\n\nView help by using parameter \'--help\'.\n')
    exit ()


if __name__ == "__main__":
    main ()
