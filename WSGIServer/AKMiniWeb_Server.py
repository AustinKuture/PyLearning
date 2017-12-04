import socket
import sys
import re
import os
from multiprocessing import Process

"""

    1 创建服务器类
    2 创建套接字并进行相关设置
    3 监听客户请求
    4 开辟相应客户请求数量的进程
    5 客户端套接字处理方法
    6 判断用户请求类型，动态or静态
    7 动态时导入应用框架，并调用方法
    8 应用框架进行处理返回请求状态及响应体
    9 响应客户端请求返回请求数据
    10 对服务器进行二次封装

"""


# 创建符合WSGI的服务器类
class WSGI_server_tcp(object):

    __response_source = []

    # 初始化
    def __init__(self, port, apps):

        # 创建套接字
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 重用地址
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self._server_socket.bind(('', port))
        # 设置服务器为监听状态
        self._server_socket.listen(128)
        # 响应头
        self.__response_headers = ''
        # web框架应用
        self.__apps = apps

    # 客户端响应处理方法
    def _client_response_deal(self, client_socket):

        # 接收客户请求
        reciv_data = client_socket.recv(2048).decode()

        # 获取客户端请求路径
        result = re.match(r'.+\s(/.*?)\s', reciv_data)

        client_path = result.group(1)

        # 拼接根路径
        if client_path is '/': client_path = '/index.html'

        # 判断资源类型
        if client_path.endswith('.py'):

            # 保存用户请求路径
            enviro = {'PATH_INFO':client_path}

            # 调用web框架并传入参数
            response_body = self.__apps(enviro, self._dynamic_source_deal)

            # 动态资源请求头
            response_line = 'HTTP/1.1 OK \r\n'
            self.__response_headers = response_line + self.__response_headers + '\r\n' + response_body

            # 返回客户端请求数据
            client_socket.send(self.__response_headers.encode())
            client_socket.close()

        # 判断静态资源
        elif client_path.endswith('.html'):

            client_path = 'Static_Source' + client_path
            self._static_source_deal(client_socket, client_path)

        # 处理错误资源
        else:

            client_path = 'Error/404.html'
            self._static_source_deal(client_socket, client_path)

    # 静态资源处理方法
    def _static_source_deal(self, client_socket, client_path):

        response_body = ''
        # 读取文件
        try:

            with open(client_path, 'rb') as readf:

                content = readf.read()
            readf.close()
        except Exception as error:

            print(error)
            client_path = 'Error/404.html'
            self._static_source_deal(client_socket, client_path)
            return
        else:

            response_body = content.decode()

        # 响应头
        response_line = 'HTTP/1.1 OK \r\n'
        response_header = 'Content-Type : text/html\r\n'
        responses = response_line + response_header + '\r\n' + response_body

        client_socket.send(responses.encode())
        client_socket.close()

    # 动态资源处理方法
    def _dynamic_source_deal(self, status, hearders):

        # 响应头
        self.__response_headers += status

        for line in hearders:

            h_key, v_key = line
            self.__response_headers += '%s : %s\r\n' % (h_key, v_key)

    # 监听客户请求
    def start_runing(self):

        while True:

            # 获取客户端套接字及客户端请求地址
            client_socket, address = self._server_socket.accept()
            print('%s正在连接...' %str(address))

            # 设置客户端请求超时时间
            client_socket.settimeout(5)

            # 为客户端请求创建相应的进程
            client_process = Process(target=self._client_response_deal, args=(client_socket,))
            client_process.start()

            client_socket.close()


if __name__ == '__main__':

    try:

        if len(sys.argv) == 3:

            # 获取端口并进行判断
            server_port = sys.argv[1]
            if server_port.isdigit():

                server_port = int(server_port)
            else:

                raise Exception('Error : 端口格式错误,应为全数字')

            # 模块名与web框架应用名
            web_module_all = sys.argv[2]

            # 截取模块名及框架应用名
            if web_module_all.count(':') > 0:

                module_index = web_module_all.index(':')
                module_name = web_module_all[:module_index]
                apps_name = web_module_all[module_index + 1:]

                if not (module_name + '.py') in os.listdir():

                    raise Exception('未找到框架模块')

                # 引入模块与框架应用对象
                web_module = __import__(module_name)
                apps = getattr(web_module, apps_name)

                # 实例化服务器对象并开始执行
                web_servers = WSGI_server_tcp(server_port, apps)
                web_servers.start_runing()

            else:

                raise Exception('Error : 模块名及框架应用名参数格式错误')
        else:

            raise Exception('Error : 输入格式错误，参数数量错误')
    except Exception as error:

        print(error)
        print('正确的格式为： python3 xx.py port modulename:apps')




























