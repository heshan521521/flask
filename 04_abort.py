#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : abort 的用法


from flask import Flask,abort,Response

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/login')
def login():
    name = "zhangsan"
    pwd = "123456"

    if name != "admin" or pwd != "admin":
        """使用abort函数可以立即终止函数的运行，并且可以返回特定的信息给前端"""
        # # 1、传递状态码信息，注意：状态码必须是标准的http状态码
        # abort(400)
        # 2、传递响应体信息
        resp = Response("login faild ,please check your name or pwd!")
        abort(resp)
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)
