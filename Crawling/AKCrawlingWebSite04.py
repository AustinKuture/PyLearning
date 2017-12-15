import urllib
import socket
import gevent
from gevent import monkey
monkey.patch_all()
from random import randint
from threading import Thread
from multiprocessing import Process
from urllib.request import urlopen


def obtain_ip_one():

    for num in range(1000):

        i = randint(1, 256)
        j = randint(1, 256)
        m = randint(1, 256)
        n = randint(1, 256)
        result = ''
        socket.setdefaulttimeout(2.5)
        try:

            url = 'http://freegeoip.net/json/%s.%s.%s.%s' % (i, j, m, n)
            send_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive'
            }
            req = urllib.request.Request(url, headers=send_headers)
            result = urlopen(req)

        except Exception as errors:

            # print('Request===:', errors)
            pass

        try:

            with open('world_ip.txt', 'a') as sf:

                sf.write(result.read().decode())
        except Exception as error:

            # print('File+++:', error)
            pass
        else:

            print('保存...', i,j,m,n)

    gevent.sleep()


# 协程
def gevent_ip():

    g_list = []
    for i in range(100):

        g = gevent.spawn(obtain_ip_one)
        g_list.append(g)

    gevent.joinall(g_list)


if __name__ == '__main__':

    pro = Process
    thd = Thread
    for i in range(4):

        for j in range(100):

            thd = Thread(target=obtain_ip_one)
            thd.start()

        pro = Process(target=gevent_ip)
        pro.start()

        print('===')
    print('创建完成')

    # pro.join()
    thd.join()



















