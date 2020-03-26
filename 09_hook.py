#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : hook 的用法


from flask import Flask,session

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/index")
def index():
    print("index 被执行")
    # a = 1 / 0
    return "index page"

@app.before_first_request
def handler_befor_first_requst():
    """在第一次请求处理前被执行"""
    print("handler_befor_first_requst 被执行")

@app.before_request
def handler_befor_requst():
    """每一次请求处理前被执行"""
    print("handler_befor_requst 被执行")

@app.after_request
def handler_after_requst(response):
    """在每一次请求（视图函数）处理之后被执行，前提是视图函数没有异常"""
    print("handler_after_requst 被执行 。返回值为 %s" %response)
    return response

@app.teardown_request
def handler_teardown_requst(response):
    """在每一次请求（视图函数）处理之后被执行，无论视图函数有没有异常，都被执行。。注意：teardown_request只工作在非调试模式，即debug=false时。"""
    print("handler_teardown_requst 被执行 。返回值为 %s" %response)
    return response

if __name__ == '__main__':
    app.run()
