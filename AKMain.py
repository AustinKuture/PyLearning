#coding=utf-8
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 主程序入口
def download_html(url):

    url_data = urlopen(url)

    bs_obj = BeautifulSoup(url_data, 'lxml')

    for link in bs_obj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):

        link = link.find('div', {'id', 'bodyContent'})

        if 'href' in link.attrs:

            print(link.attrs['href'])




# download_html('http://www.pythonscraping.com/pages/warandpeace.html')
# download_html('http://www.pythonscraping.com/pages/page3.html')

download_html('http://en.wikipedia.org/wiki/Kevin_Bacon')
