import json
from time import sleep
from pymysql import *
from threading import Thread


# 创建数据库连接
qeury_connec = connect(host='localhost',
                 port=3306,
                 user='root',
                 password='kkl',
                 db='World_IP',
                 charset='utf8')


def save_data(ip, country_code, country_name, region_code,
              region_name, city, zip_code, time_zone, latitude,
              longitude, metro_code):

    print('++++',ip, country_code, country_name, region_code,
              region_name, city, zip_code, time_zone, latitude,
              longitude, metro_code)
    try:

        # 开始保存数据
        # 创建游标
        qeury_cursor = qeury_connec.cursor()
        save_sql = 'INSERT INTO world_ip (ip, country_code, country_name, region_code, region_name, city, zip_code, time_zone, latitude, longitude, metro_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        qeury_cursor.execute(save_sql, [ip, country_code, country_name, region_code,
              region_name, city, zip_code, time_zone, latitude,
              longitude, metro_code])
    except Exception as error:

        print('===',error)
    else:

        if qeury_cursor:

            print('%s saved...' % ip)

        qeury_connec.commit()
    finally:

        # 关闭游标及连接
        qeury_cursor.close()


ip_use_list = ['ip', 'country_code', 'country_name', 'region_code', 'region_name',
               'city', 'zip_code', 'time_zone', 'latitude', 'longitude', 'metro_code']
# 返回处理好的元组
def json_deal(line):

    back_list = []
    deal_json = json.loads(line)

    for ips in ip_use_list:

        keys = deal_json.get(ips)
        back_list.append(keys)

    return tuple(back_list)


# 读取文件数据
def read_data_file():

    try:

        with open('new_world_ip.txt', 'r') as rf:

            content = rf.readlines()

    except Exception as error:

        print(error)
    else:

        # thd = Thread
        for line in content:

            ip_tuple = json_deal(line)
            # thd = Thread(target=save_data, args=ip_tuple)
            # thd.start()
            ip, country_code, country_name, region_code,region_name, city, zip_code, time_zone, latitude,longitude, metro_cod=ip_tuple
            save_data(ip, country_code, country_name, region_code,region_name, city, zip_code, time_zone, latitude,longitude, metro_cod)

        # thd.join()


read_data_file()

qeury_connec.close()























