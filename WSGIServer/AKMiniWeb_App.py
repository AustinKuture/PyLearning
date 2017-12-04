#coding=utf-8
# 创建符合WSGI协议的引用函数
def applications(enviro, start_response):

    print(enviro['PATH_INFO'])

    start_response('200 OK\r\n',[('Servername', 'PythonServer v1.0.0')])

    return 'Kuture'


























