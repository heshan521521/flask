#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/15
# @Desc  :

from flask import Flask,request

app = Flask(__name__)

@app.route("/index" , methods=["GET","POST"])
def index():
    #request包含了前端发送过来的所有请求数据
    #通过request.form可以直接提取请求体中的表单格式数据，是一个类字典的对象
    #通过get方法只能拿到同名参数的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    name_list = request.form.getlist("name")
    print('request.data:%s ' %(request.data))

    #args参数是用来获取usl中的参数（查询字符串）
    city = request.args.get("city")
    return "hello name = %s,age = %s,city = %s ,name_list = %s" %(name, age, city, name_list)

if __name__ == "__main__":
    app.run(debug=True)