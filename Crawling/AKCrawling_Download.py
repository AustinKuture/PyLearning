import re
import random
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen('https://www.jd.com/')
bsObj = BeautifulSoup(html, 'lxml')
all = bsObj.findAll(src=True)

links = []

for line in all:

    print(line)
    line = line.decode()

    # result = re.search('.*src="(http|//)(.*)(www(.*)(jpg|png|gif|mp4))"\S',line)
    result = re.search('www(.*?)(png|jpg|gif)', line)
    if result:

        # print('=====', result.group())
        if result.group() not in links:

            links.append(result.group())
            urls = 'http://' + result.group()
            end_files = re.match('.*(\..{3,5})', urls)
            urlretrieve(urls, 'DownPic/' + str(random.randint(0, 1000)) + end_files.group(1))
