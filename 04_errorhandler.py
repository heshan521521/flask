#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : errorhandler 的用法


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
        abort(404)
    return 'Hello World!'


#接上一个函数，自定义错误处理方法处理abort(404)的方式
@app.errorhandler(404)
def handler_404_err(err):
    """自定义错误信息"""
    return "哎呀，天蹋啦，%s" %err


if __name__ == '__main__':
    app.run(debug=True)
