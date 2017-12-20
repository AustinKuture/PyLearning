import re
import socket
from random import randint
from time import sleep
from bs4 import BeautifulSoup
from urllib import request
from threading import Thread
from multiprocessing import Process


# <tr align="middle">
# <td><a href="http://qq.ip138.com/idsearch/" target="_blank">身份证号码查询验证</a></td>
# <td><a href="http://www.ip138.com/ems/" target="_blank">快递查询</a> <a href="http://www.ip138.com/ems/" target="_blank">EMS查询</a></td>
# <td><a href="http://www.ip138.com/carlist.htm" target="_blank">全国各地车牌查询表</a></td>
# <td><a href="http://www.ip138.com/weizhang.htm" target="_blank">车辆交通违章查询</a></td>

# http://www.ip138.com/ips1388.asp?ip=85.33.8.96&action=2
# agent_ip = Random_Proxy()
# agent_ip_list = agent_ip.obtain_agent_ip('http://ip.chinaz.com/getip.aspx')


def obtain_ip(ip):

    try:

        socket.setdefaulttimeout(5)

        agent_header_list = ["Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) ",
                            "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) ",
                            "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 ) ",
                            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) ",
                            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG) ",
                            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.0.3705) ",
                            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0 ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1 ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.00 ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; TencentTraveler ) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.0 ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.50 ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; FDM) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; MathPlayer 2.0; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; {FF0C8E09-3C86-44CB-834A-B8CEEC80A1D7}; iOpus-I-M) ",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; i-Nav 3.0.1.0F; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040616 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.5) Gecko/20031007 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; m18) Gecko/20010131 Netscape6/6.01 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/7.0.0 Safari/700.13 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.53 Safari/534.3 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 ",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 "]


        url = 'http://www.ip138.com/ips1388.asp?ip=%s&action=2' %ip

        # 创建代理处理
        proxy_hander = request.ProxyHandler({"http":"http://219.155.204.23:8080"})

        # 创建opener
        proxy_opener = request.build_opener(proxy_hander)

        # 创建用户代理
        proxy_opener.addheaders = [('User-Agent','%s'%agent_header_list[randint(0,len(agent_header_list)-1)])]

        # 安装opener
        request.install_opener(proxy_opener)

        result_html = request.urlopen(url).read()

        bsObj = BeautifulSoup(result_html, 'lxml')

        result = bsObj.findAll('table', align=re.compile('center'), width='80%')

        split = str(result).splitlines()

        for line in split:

            ip_res = re.match('.*本站数据：(.*?\s)',line)

            rf = ''
            if ip_res:

                try:

                    with open('Single_ip_add.txt', 'a') as rf:

                        rf.write('{%s:%s}\n' %(ip,ip_res.group(1)))
                except Exception as error:

                    # print(error)
                    rf.close()
                else:

                    print('IP:%s-----地址：%s' % (ip, ip_res.group(1)))
    except Exception as error:

        # print(error)

        pass
def start_scrap():

    for ra in range(200):

        i = randint(1, 256)
        j = randint(1, 256)
        m = randint(1, 256)
        n = randint(1, 256)

        obtain_ip('%d.%d.%d.%d' % (i, j, m, n))
        sleep(randint(1, 10) * 0.01)

def start_thd():

    thd_list = []
    for thd in range(1000):

        sun_thd = Thread(target=start_scrap)
        sun_thd.start()
        thd_list.append(sun_thd)

    print('-----线程创建完成')
    for thd_end in thd_list:

        thd_end.join()
    print('+++++线程已运行完成')


# 创建进程并开始爬取
def creat_pro():

    pro_lsit = []
    for i in range(5):

        pro = Process(target=start_thd)
        pro.start()

        pro_lsit.append(pro)
    print('=====', '进程创建完成')

    for pro_end in pro_lsit:

        pro_end.join()

    print('======爬取完成')

creat_pro()


















