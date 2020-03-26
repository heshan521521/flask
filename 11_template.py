#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : template模板 的用法


from flask import Flask,render_template
from flask_script import Manager #启动命令的管理类

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/index")
def index():
    # 方法一
    # return  render_template("index.html", name = "python" , age = 18)
    # 方法二，使用django的思想，先定义字典，再传入
    # data = {
    #     "name":"python1",
    #     "age":19
    # }
    # #注意：**data 就是将字典进行解包
    # return render_template("index.html", **data)
    data = {
        "name": "python1",
        "age": 19 ,
        "my_dict": {"city":"hangzhou"},
        "my_list": [1 , 2, 3, 4,5],
        "my_int" : 0
    }
    # 注意：**data 就是将字典进行解包
    return render_template("index.html", **data)

def list_step_2(li):
    """自定义过滤器，功能为获取列表中步长为2的数据"""
    # 利用切片的方式从左到右进行处理
    return li[::2]

#注册过滤器
#方法一
app.add_template_filter(list_step_2, "li2")

#方法二，通过装饰器进行处理 template_filter("模板中使用的装饰器名字")
@app.template_filter("li3")
def list_step_3(li):
    """自定义过滤器，功能为获取列表中步长为2的数据"""
    # 利用切片的方式从左到右进行处理
    return li[::3]

if __name__ == '__main__':
    app.run(debug=True)