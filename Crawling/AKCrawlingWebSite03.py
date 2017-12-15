
import re
import random
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen


pages = set()
random.seed(datetime.datetime.now())


#获取页面所有的内链列表
def getInternalLinks(bsObj, includeUrl):

    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internaLinks = []

    # 找出所有以‘/‘开头的链接
    for link in bsObj.findAll("a", href=re.compile('^(/|.*"+includeUrl+")')):

        if link.attrs['href'] is not None:

            if link.attrs['href'] not in internaLinks:

                if (link.attrs['href'].startswith("/")):

                    internaLinks.append(includeUrl+link.attrs['href'])
                else:

                    internaLinks.append(link.attrs['href'])
    return internaLinks


#获取页面所有外部链接的列表
def getExternalLinks(bsObj, excludeUrl):

    externalLinks = []

    # 找出所有以’http’或‘www’开头且不包含当前URL的链接
    for link in bsObj.findAll('a',href=re.compile('^(http|www)((?!"+excludeUrl+").)*$')):

        if link.attrs['href'] is not None:

            if link.attrs['href'] not  in externalLinks:

                externalLinks.append(link.attrs['href'])
    return externalLinks


# 分解地址
def splitAddress(address):

    addressParts = address.replace('http://', '').split('/')

    return addressParts


# 随机爬取网站内容
def getRandomExternalLink(startingPage):

    try:

        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html, 'lxml')
        externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    except Exception as error:

        print(error)
    else:

        if len(externalLinks) == 0:

            print('未发现外链接， 正在从网站抓取...')
            domain = urlparse(startingPage).scheme+'://'+urlparse(startingPage).netloc
            internalLinks=getInternalLinks(bsObj, domain)

            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        else:

            return externalLinks[random.randint(0, len(externalLinks) - 1)]


# 外链的获取
def followExternalOnly(startingSite):

    externaLink = getRandomExternalLink(startingSite)

    print('随机外链接为：', externaLink)


    followExternalOnly(externaLink)


# 内链的获取
def followInternalLinks(startingSite):

    html = urlopen(startingSite)
    bsObj = BeautifulSoup(html, 'lxml')
    internalLink = getInternalLinks(bsObj, urlparse(startingSite).netloc)

    print(internalLink)



    if len(internalLink) == 0:

        print('未发现外链接， 正在从网站抓取...')
        print('===', startingSite)
        domain = urlparse(startingSite).scheme+'://'+urlparse(startingSite).netloc
        internalLinks=getInternalLinks(bsObj, domain)

        return followInternalLinks(internalLinks[random.randint(0, len(internalLinks) - 1)])


# followExternalOnly('http://oreilly.com')
# followInternalLinks('http://kuture.com.cn')
# followExternalOnly('http://www.kuture.com.cn')
# followInternalLinks('http://image.baidu.com/')
# followExternalOnly('http://image.baidu.com/')
# followInternalLinks('http://oreilly.com')
# followExternalOnly('http://www.bubuko.com')
# followExternalOnly('http://www.liuhaihua.cn')
followInternalLinks('http://www.liuhaihua.cn')















