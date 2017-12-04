from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import re

# wf = open('cocochina.txt','w')

pages = set()
def getLinks(pageUrl):

    try:

        global pages
        html = urlopen(pageUrl)
        bs_obj = BeautifulSoup(html, 'lxml')

        for link in bs_obj.findAll('a',href=re.compile('.*')):

            print(link)

            # if 'href' in link.attrs:
            #
            #     if link not in pages:
            #
            #         newPage = link.attrs['href']
            #         pages.add(newPage)
            #         getLinks(newPage)
            #
            #         print('=====', newPage)

            # if 'href' in link.attrs:
            #
            #     if link.attrs['href'] not in pages:
            #
            #         newPage = link.attrs['href']
            #         # print(newPage)
            #
            #         # wf.write(newPage)
            #         pages.add(newPage)
            #         getLinks(newPage)

    except Exception as error:

        print(error)
    #
    # finally:

        # wf.close()

                # sleep(0.001)
getLinks('https://www.tianyancha.com/')





































