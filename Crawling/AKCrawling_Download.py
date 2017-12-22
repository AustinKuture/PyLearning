import re
import os
import socket
from urllib.request import urlopen ,urlretrieve
from threading import Thread
from bs4 import BeautifulSoup
from Crawling.Main_Agent_IP.AK_AGent_IP_Data import obtain_url_html as result_html

# 存储链接
links = []
# 存储网址
web_site = []

def craw_loop(web_url):

    try:

        # 使用代理获取数据
        # res_html_obj = result_html(web_url)

        # 不使用代理获取数据
        res_html_obj = urlopen(web_url)

        bsObj = BeautifulSoup(res_html_obj, 'lxml')
        all = bsObj.findAll()
    except Exception as error:

        print('获取数据失败,错误原因:',error)
    else:
        global links
        global web_site

        all = str(all).splitlines()
        for line in all:

            # print('===', line)
            result = re.search('(http://|www|https://)(.*?)\.(png|PNG|jpg|gif)\s?', line)

            if result:

                if result.group() not in links:

                    # print('*****', result.group())

                    # 检测链接并去重
                    links.append(result.group())

                    # 修正链接格式
                    urls = result.group()
                    if not urls.startswith('http'):

                        urls = 'http://' + urls

                    # # 递归爬取
                    # if (urls.endswith('.com') or urls.endswith('.html')) and (urls not in web_site):
                    #
                    #     print('+++Jump+++',urls)
                    #     web_site.append(urls)

                    # 文件类型

                    # 后缀名
                    end_files = re.match('.*(\..{3,5})', urls)
                    # 文件名
                    pic_name = urls[urls.rfind('/')+1:urls.rfind('.')]
                    # 文件夹
                    docu_ment = 'DownLoad_Medium'
                    # 子级路径
                    web_document = web_url[web_url.find('.')+1:web_url.rfind('.')]

                    try:

                        # 判断或生成路径
                        if not os.path.exists(docu_ment):

                            os.mkdir(docu_ment)

                        if not web_document in os.listdir(docu_ment):

                            os.mkdir(docu_ment + '/' + web_document)
                    except Exception as error:

                        print('路径拼接错误...',error)
                        return

                    # 保存路径
                    docu_ment = docu_ment + '/' + web_document + '/'

                    # 下载媒体数据
                    try:

                        # 排除网站及网页
                        if not (urls.endswith('.com') or urls.endswith('.html')):

                            # 跳过已下载过的媒体文件
                            if not pic_name + end_files.group(1) in os.listdir(docu_ment):

                                medium_down_thd = Thread(target=load_pic_thd, args=(urls, docu_ment, pic_name, end_files))
                                medium_down_thd.start()
                    except Exception as error:

                        print(error)
                        continue


# 为图片下载开启线程
def load_pic_thd(medium_url, document, medium_name, medium_type):

    try:

        # 设置超时时间
        socket.setdefaulttimeout(5)
        print('正在下载...', medium_url)

        urlretrieve(medium_url, document + medium_name + medium_type.group(1))

        print('已保存---', medium_name + medium_type.group(1))
    except Exception as error:

        print('请求超时或下载失败...')
        print(error)
        return


if __name__ == '__main__':

    craw_loop('http://www.baidu.com/')

    # thd_join_list = []
    # for linkss in web_site:
    #
    #     try:
    #
    #         thd = Thread(target=craw_loop, args=(linkss,))
    #         thd.start()
    #         thd_join_list.append(thd)
    #     except Exception as error:
    #
    #         print(error)
    #         continue
    #
    # for end_thd in thd_join_list:
    #
    #     end_thd.join()

    for i in web_site:

        print(i)

    print('爬取完成')