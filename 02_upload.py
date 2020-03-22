#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/15
# @Desc  : upload

from flask import Flask,request

app = Flask(__name__)

@app.route("/upload" , methods=["POST"])
def upload():
    """接收前端传送过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # is None表示没有发送文件
        return "未上传文件，请XXXX"

    # # 将文件保存到本地
    # # 方法一：
    # # 1、创建一个文件
    # f = open("./demo.png" , "wb")
    # # 2、向文件里写内容
    # data = file_obj.read()
    # f.write(data)
    # # 3、 关闭文件
    # f.close
    # return "上传成功，请XXXX"
    # 方法二：
    # 直接将上传的文件对象保存
    file_obj.save("./demo1.png")
    return "上传成功，请XXXX"
if __name__ == "__main__":
    app.run(debug=True)