#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 14_macro.py.py
# @Author: heshan
# @Date  : 2020/3/26
# @Desc  : macro (宠)的使用

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('macro.html')


if __name__ == ("__main__"):
    app.run(debug = True)
