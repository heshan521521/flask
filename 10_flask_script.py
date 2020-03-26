#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : flask_script 的用法


from flask import Flask
from flask_script import Manager #启动命令的管理类

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

#创建manager的管理类的对象
manager = Manager(app)

@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()