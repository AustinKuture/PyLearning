import urllib
from urllib.request import urlopen
from urllib import request, parse

url = 'http://www.baidu.com'
send_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}
req = urllib.request.Request(url, headers=send_headers)
result = urlopen(req)

print(result.read())
