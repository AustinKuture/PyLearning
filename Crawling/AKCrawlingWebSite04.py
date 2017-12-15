import time
import socket
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
        socket.setdefaulttimeout(2)
        try:
            result = urlopen('http://freegeoip.net/json/%s.%s.%s.%s' %(i,j,m,n))
        except Exception as errors:

            # print('Request===:', errors)
            n+=1

        try:
            with open('world_ip.txt', 'a') as sf:

                sf.write(result.read().decode())
        except Exception as error:

            # print(error)
            pass
        else:

            print('保存...', i,j,m,n)


def pro_ip():

    thd = Thread
    for i in range(1000):

        thd = Thread(target=obtain_ip_one)
        thd.start()

        # print('线程：', i)

    thd.join()


if __name__ == '__main__':

    pro = Process
    for i in range(8):

        pro = Process(target=pro_ip)
        pro.start()
        # print('进程：', i)

    pro.join()



















