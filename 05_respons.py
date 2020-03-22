#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : Response 的用法


from flask import Flask,abort,Response,make_response

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/index')
def index():
    """1、使用元祖返回自定义响应信息"""
    # 本来return"index page" 时状态码为200，修改后，返回状态码为400
    # "index page"为响应体，400为状态码，[("ITCAST","PYTHON"),("city","shenzhen")]为响应头.注意：元祖信息中如果为中文会报错。
    # return ("index page",400,[("ITCAST","PYTHON"),("city","shenzhen"),("addrs","zhangsanlu 1058")])
    # 或者
    # return "index page", 400, [("ITCAST", "PYTHON"), ("city", "shenzhen"), ("addrs", "zhangsanlu 1058")]
    # 或者 使用字典
    # return "index page", 400, {"ITCAST":"PYTHON", "city":"shenzhen", "addrs":"zhangsanlu 1058"}
    # 或者 使用自定义状态码
    # return "index page", 666, {"ITCAST":"PYTHON", "city":"shenzhen", "addrs":"zhangsanlu 1058"}
    # 或者 使用自定义状态码
    # return "index page", "666 itcast status", {"ITCAST": "PYTHON", "city": "shenzhen", "addrs": "zhangsanlu 1058"}
    """2、使用 make response 来构造响应信息"""
    resp = make_response("index page 2")
    resp.status = "999 itcast status."
    resp.headers["city"] = "hangzhou"
    return resp




if __name__ == '__main__':
    app.run(debug=True)
