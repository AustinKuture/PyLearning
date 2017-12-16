import socket
from urllib import request



socket.setdefaulttimeout(3)

ip_port_list = get_IP()
url = 'http://ip.chinaz.com/getip.aspx'

for proxys in ip_port_list:


    try:
        # 创建代理处理
        proxy_hander = request.ProxyHandler(eval(proxys))

        # 创建opener
        proxy_opener = request.build_opener(proxy_hander)

        # 创建用户代理
        proxy_opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/56.0.2924.87 Safari/537.36')]

        # 安装opener
        request.install_opener(proxy_opener)

        result = request.urlopen(url).read().decode()

        print('%s...链接畅通...获取的内容为：%s' % (proxys, result))
    except Exception as error:

        # print('%s...%s' %(proxys, error))
        continue




























