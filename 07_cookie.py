#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : cookie 的用法


from flask import Flask,Response,make_response,request

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

##设置cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("success")
    #设置cookie,默认有效期是浏览器关闭就失效
    resp.set_cookie("ITCAST","python")
    resp.set_cookie("ITCAST1", "python1")
    #通过max_age设计有效期
    resp.set_cookie("ITCAST2", "python2", max_age = 3600)
    # 通过修改headers的方法设置cookie
    resp.headers["Set-Cookie"] = "ITCAST3=python3; Expires=Wed, 25-Mar-2020 09:42:07 GMT; Max-Age=3600; Path=/"
    return resp

#获取cookie
@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get("ITCAST")
    return c


#删除cookie
@app.route('/del_cookie')
def del_cookie():
    resp = make_response("del success")
    #删除cookie
    resp.delete_cookie('ITCAST')

    return resp

if __name__ == '__main__':
    app.run(debug=True)
