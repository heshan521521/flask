#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : session 的用法


from flask import Flask,session

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

#flask默认把session数据保存到cookie中

#设置session之前需要设置一个flask用到的密钥
app.config["SECRET_KEY"] = "JKSADFJ;DSAKF;LKLDSA;FJJ"

@app.route('/login')
def login():
    #设置session数据
    session['name'] = "python"
    session['mobile'] = "13588158899"
    return "login success"


@app.route('/index')
def index():
    #获取ession数据
    name = session.get("name")
    return "get success.the session is %s" %(name)

if __name__ == '__main__':
    app.run(debug=True)
