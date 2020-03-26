#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : template模板 的用法


from flask import Flask,request,render_template
from flask_script import Manager #启动命令的管理类

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route("/xss" , methods=["GET","POST"])
def xss():
    text = ""
    if request.method=="POST":
        text = request.form.get("text")

    return render_template("xss.html", text = text)

    # 注意：**data 就是将字典进行解包
    # return render_template("index.html", **data)

if __name__ == '__main__':
    app.run(debug=True)