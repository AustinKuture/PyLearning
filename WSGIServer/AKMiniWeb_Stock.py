import re
from pymysql import *


# 路由地址列表
route_list = []


# 请求路径装饰器
def path_route(path_info):

    def inners(func):

        # 拼接路径与引用函数
        route_list.append((path_info, func))

        def checks(*args, **kwargs):

            return func(*args, **kwargs)
        return checks
    return inners


@path_route('/index.py')
def func_index(filename):

    # 使用sql语句从数据库读取数据
    html_mysql_data = change_data_mysql('SELECT * from info')

    return  create_mysql_html(html_mysql_data, filename)


@path_route('/center.py')
def func_center(filename):

    # 使用sql语句从数据库读取数据
    html_mysql_data = change_data_mysql('select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id = f.info_id')

    return create_mysql_html(html_mysql_data, filename)


@path_route('/update.py')
def func_update(filename):

    return read_file(filename)


@ path_route('/login.py')
def func_login(filename):

    return read_file(filename)


#封装文件读取
def read_file(files):

    try:
        files = files.replace('.py', '.html')
        with open('./Dynamic' + files) as r_files:

            file_data = r_files.read()
        r_files.close()
    except Exception as error:

        print(error)
        return
    else:

        return file_data


# 从数据库读取数据
def change_data_mysql(sqls):

    # 创建数据库连接
    data_connect = connect(
        host='localhost',
        port=3306,
        user='root',
        password='kkl',
        database='stock_db',
        charset='utf8'
    )

    # 创建游标
    data_cursors = data_connect.cursor()
    # 执行sql语句
    data_cursors.execute(sqls)
    data_result = data_cursors.fetchall()

    return data_result


# 生成读取内容的html数据
def create_mysql_html(orignal_html, file_name):

    result_html = ''

    for lines in orignal_html:
        line_str = """<tr>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>%s</td>
                                  <td>
                                      <a type="button" class="btn btn-default btn-xs" href="/update.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                                  </td>
                                  <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
                              </tr>
                              """ % (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6])

        result_html += line_str

    result = re.sub('{%content%}', result_html, read_file(file_name))  # read_file 读取指定文件内容

    return result


# 创建符合WSGI协议的引用函数
def applications(enviro, start_response):

    path_info = enviro['PATH_INFO']
    respone_body = '<h1 style="text-align: center;color:blue"> Bad 404 </h1>'

    for url, func in route_list:

        new_url = url.replace('.py', '.html')

        if path_info in (url,new_url):

            respone_body = func(path_info)

    start_response('200 OK\r\n',[('Servername', 'PythonServer v1.0.0')])

    return respone_body






































