import re
from random import randint
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Process
from urllib.request import urlopen, urlretrieve


# <tr align="middle">
# <td><a href="http://qq.ip138.com/idsearch/" target="_blank">身份证号码查询验证</a></td>
# <td><a href="http://www.ip138.com/ems/" target="_blank">快递查询</a> <a href="http://www.ip138.com/ems/" target="_blank">EMS查询</a></td>
# <td><a href="http://www.ip138.com/carlist.htm" target="_blank">全国各地车牌查询表</a></td>
# <td><a href="http://www.ip138.com/weizhang.htm" target="_blank">车辆交通违章查询</a></td>

# http://www.ip138.com/ips1388.asp?ip=85.33.8.96&action=2

def obtain_ip(ip):

    print('+++')
    try:
        html = urlopen('http://www.ip138.com/ips1388.asp?ip=%s&action=2' %ip)
        bsObj = BeautifulSoup(html, 'lxml')

        result = bsObj.findAll('table', align=re.compile('center'), width='80%')

        split = str(result).splitlines()
        print(ip)
        print('+_+_+_', split)

        for line in split:

            ip_res = re.match('.*本站数据：(.*?\s)',line)

            rf = ''
            if ip_res:

                try:

                    with open('Single_ip_add.txt', 'a') as rf:

                        rf.write('{%s:%s}\n' %(ip,ip_res.group(1)))
                except Exception as error:

                    print(error)
                    rf.close()
                else:

                    print('IP:%s-----地址：%s' % (ip, ip_res.group(1)))
    except Exception as error:

        print(error)


def start_scrap():

    for ra in range(1):

        i = randint(1, 256)
        j = randint(1, 256)
        m = randint(1, 256)
        n = randint(1, 256)

        obtain_ip('%d.%d.%d.%d' % (i, j, m, n))
        sleep(randint(1, 10) * 0.01)


# 创建进程并开始爬取
pro = Process
for i in range(8):

    pro = Process(target=start_scrap)
    pro.start()
    print('---', i)

pro.join()
print('======爬取完成')



















