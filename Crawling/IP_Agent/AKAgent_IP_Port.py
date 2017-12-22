#encoding=utf8
import re
import socket
from time import sleep
from random import randint
from urllib import request
from bs4 import BeautifulSoup
from multiprocessing import Process, Manager

# 获取可用代理
class Random_Proxy(object):


    # 为代理获取开辟进程
    def __agent_ip_pro(self, num,request_url, back_list):

        print('当前进程......%s' % num)
        # 创建代理处理
        proxy_hander = request.ProxyHandler({"http": "http://60.12.126.145:8080"})

        # 创建opener
        proxy_opener = request.build_opener(proxy_hander)

        # 创建用户代理
        proxy_opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322)')]

        # 安装opener
        request.install_opener(proxy_opener)

        # agent_url = ''
        try:

            res = request.urlopen('http://www.xicidaili.com/nn').read()

            print(res)
            # agent_url = 'http://www.xicidaili.com/nn/'
            # res = request.urlopen(agent_url).read()
        except Exception as error:

            print('代理网站(%s)异常或目标地址链接失效...%s'%('',error))
        else:

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
                        ip_port = '{"http":"http://%s:%s"}' % (scrap_ip.group(1), scrap_ip.group(2))
                        ip_port_list.append(ip_port)

            except Exception as error:

                print('数据爬取失败...', error)
            else:

                # return self.__check_ip_agent(request_url, ip_port_list)
                ip_agent_list = self.__check_ip_agent(request_url, ip_port_list)
                for line in ip_agent_list:

                    back_list.append(line)



    # 获取代理IP及端口
    def obtain_agent_ip(self, request_url):

        # 进程通信，获取进程函数的返回值
        print('代理初始化,正获取代理中...')
        manager = Manager()
        back_list = manager.list()
        pro_list = []

        for i in range(1,2):

            ip_pro = Process(target=self.__agent_ip_pro, args=(i, request_url, back_list))
            ip_pro.start()

            pro_list.append(ip_pro)

            sleep(randint(1,10) * 0.1)

        # 阻塞等待进程结束
        for pro_end in pro_list:

            pro_end.join()

        print('代理获取完成...')
        return back_list

    # 验证IP的正确性
    def __check_ip_agent(self, url, ip_list):

        checked_ip_port_list = []

        sf = None
        try:

            sf = open('./Sys_File/agent_ip.txt', 'a')
        except Exception as error:

            sf.close()
            sf = None
            print('文件路径不存在...%s', error)

        for proxys in ip_list:

            try:

                socket.setdefaulttimeout(randint(10,20) * 0.1)

                # 创建代理处理
                proxy_hander = request.ProxyHandler(eval(proxys))

                # 创建opener
                proxy_opener = request.build_opener(proxy_hander)

                # 创建用户代理
                proxy_opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                                                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                          'Chrome/56.0.2924.87 Safari/537.36')]

                # 安装opener
                request.install_opener(proxy_opener)

                result = request.urlopen(url).read().decode()

                print('%s...链接畅通...获取的内容为：%s' % (proxys, result))
            except Exception as error:

                print('%s...%s' %(proxys, error))
                if sf is not None:

                    sf.write('%s---代理异常或无法使用\n' %proxys)
                continue
            else:

                if sf is not None:
                    sf.write('%s-------^_^------->代理可用，链接畅通\n' % proxys)
                checked_ip_port_list.append(eval(proxys))

        sf.close()

        return checked_ip_port_list


if __name__ == '__main__':

    url = 'http://ip.chinaz.com/getip.aspx'
    get_agent = Random_Proxy()

    all_agent_list =  get_agent.obtain_agent_ip(url)

    print('===', all_agent_list)



















