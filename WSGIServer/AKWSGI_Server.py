import os
from wsgiref.simple_server import make_server


def application(environment, start_response):

    print(environment['PATH_INFO'])

    user_request = str(environment['PATH_INFO'])

    if user_request.endswith('.py'):

        print('正在请求动态资源...')
        # Web 服务器响应函数的调用
        start_response('200 OK', [('Content-Type', 'text/html')])

        dir_list = os.listdir()
        res_path = environment['PATH_INFO']
        res_path = str(res_path).replace('/','')
        if res_path in dir_list:

            with open(res_path, 'r') as rf:

                content = rf.read()
            # 请求体
            response_body = '<h1>您请求的为动态资源<br/>' \
                            '请求路径为:%s<br/>' \
                            '请求的资源为:%s</h1>' %(user_request, content)

            # 返回请求的结果
            return [response_body.encode()]
        else:

            # 请求体
            response_body = '<h1>未查找到相关资源</h1>'

            # 返回请求的结果
            return [response_body.encode()]
    elif user_request.endswith('.html'):

        print('正在请求静态资源...')
        # Web 服务器响应函数的调用
        start_response('200 OK', [('Content-Type', 'text/html')])

        # 请求体
        response_body = '<h1>您请求的为静态资源<br/>请求路径为:%s</h1>' % user_request

        # 返回请求的结果
        return [response_body.encode()]

    else:

        print('请求的资源有误！')

        # Web 服务器响应函数的调用
        try:

            start_response('404 NOTFOUND', [('Content-Type', 'text/html')])
        except Exception as error:

            print(error)

        # 请求体
        response_body = r'<h1>404 NOTFOUND</h1>'

        # 返回请求的结果
        return [response_body.encode()]


http_server = make_server('127.0.0.1', 8080, application)

print('服务器正在监听8080端口...')

http_server.serve_forever()






















