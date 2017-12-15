import re
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen('http://www.sina.com')
bsObj = BeautifulSoup(html, 'lxml')
all = bsObj.findAll(src=True)

for line in all:

    line = line.decode()

    result = re.match('.*src="(http|//)(.*)(www(.*)(jpg|png|gif|mp4))"\S',line)
    if result:

        print(result.group(3))