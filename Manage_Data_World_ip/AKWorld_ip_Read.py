import os
import json
import time
from threading import Thread


rf = ''

new_world_ip = []


def thd_ip(line):

    ip_k = json.loads(line)
    user_ip = ip_k.get('ip')
    wf = ''
    if user_ip not in new_world_ip:

        new_world_ip.append(user_ip)
        try:
            with open('../Crawling/new_world_ip.txt', 'a') as wf:

                wf.write(line)
        except Exception as error:

            print(error)
        else:

            print(user_ip + 'is from :' + ip_k.get('country_code'))
        finally:

            wf.close()


try:

    with open('../Crawling/world_ip.txt', 'r') as rf:

        content = rf.readlines()
    print(len(content))
except Exception as error:

    print(error)
else:

    for line in content:

        thd = Thread(target=thd_ip, args=(line,))
        thd.start()



    # print(len(new_world_ip))






































