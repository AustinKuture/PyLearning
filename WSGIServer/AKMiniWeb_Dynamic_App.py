import re

# 验证装饰器
def login_check(func):

    def check(*args, **kwargs):

        path = args[0]
        print('======', path)
        if path in ('/login.py', '/login.html'):

            path = 'static' + str(path).replace('.py', '.html')
            try:

                with open(path) as rf:

                    content = rf.read()
            except Exception as error:

                print(error)
            else:

                func(path)
                return content
        else:

            path = 'static' + str(path).replace('.py', '.html')

            try:

                with open(path) as rf:

                    content = rf.read()
            except Exception as error:

                print(error)
            else:

                return func(content)

    return check


# 账号登陆
@login_check
def login_account(path_info):

    print('登陆成功\n路径：', path_info)
    return


@login_check
def get_runtimes(content):

    result = re.sub('{context}', 'Kuture', content)
    if result:

        return result
    else:

        return '<h1 style="text-align: center">404</h1>'


# 存储路由地址
route_list = [

    ('/login.py', login_account),
    ('/runtimes.py', get_runtimes)
]


# 创建符合WSGI协议的引用函数
def applications(enviro, start_response):

    path_info = enviro['PATH_INFO']
    respone_body = '<h1> Bad 404 </h1>'

    for url, func in route_list:

        new_url = url.replace('.py', '.html')
        if path_info == url or path_info == new_url:

            respone_body = func(url)

    start_response('200 OK\r\n',[('Servername', 'PythonServer v1.0.0')])

    return respone_body


























