#encoding=utf8
import re
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve


# 获取代理IP及端口
def obtain_agent_ip():

    User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    header = {}
    header['User-Agent'] = User_Agent

    url = 'http://www.xicidaili.com/nn/1'
    req = urllib.request.Request(url, headers=header)
    res = urlopen(req).read()

    ip_port_list = []
    try:
        # 创建soup对象
        soup = BeautifulSoup(res, 'lxml')
        ips = soup.findAll('tr')

        for line in ips:

            # 获取所有td标签
            ip_td = line.findAll('td')

            # 爬取IP及端口
            scrap_ip = re.search('(\d*\.\d*\.\d*\.\d*).{5,11}<td>(\d*)', str(ip_td))

            if scrap_ip:

                ip_port = '{ip:%s,port: %s}' % (scrap_ip.group(1), scrap_ip.group(2))
                ip_port_list.append(ip_port)
    except Exception as error:

        print('数据爬取失败...', error)
    else:

        sf = ''
        try:

            with open('./Sys_File/agent_ip.txt', 'a') as sf:

                for lines in ip_port_list:

                    sf.write(lines+'\n')
        except Exception as error:

            print('写入数据失败...', error)
            return
        else:

            return ip_port_list
        finally:

            sf.close()


if __name__ == '__main__':

    all_ip = obtain_agent_ip()

    for line in all_ip:

        print(line)