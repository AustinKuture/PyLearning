import socket
from random import randint
from urllib import request


def obtain_url_html(url):

    try:

        # socket.setdefaulttimeout(5)

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


        # 创建代理处理
        proxy_hander = request.ProxyHandler({"http":"http://222.182.53.114:8118"})

        # 创建opener
        proxy_opener = request.build_opener(proxy_hander)

        # 创建用户代理
        proxy_opener.addheaders = [('User-Agent','%s'%agent_header_list[randint(0,len(agent_header_list)-1)])]

        # 安装opener
        request.install_opener(proxy_opener)

        result_html = request.urlopen(url)
        print('响应对象:%s 正在处理数据...' %result_html)
    except Exception as error:

        print(error)
        raise Exception('数据异常,请检查代理或链接是否有效')

    else:

        return result_html

























