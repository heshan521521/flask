#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : converter_mini_demo.py.py
# @Author: heshan
# @Date  : 2020/3/15
# @Desc  : 自定义一个手机号的转换器

from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# --=====手机号的转换器=============================================================
# 1、自定义手机号的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter,self).__init__(url_map)
        # 正则表达式：r'1[34578]\d{9}'，表示1开头，且第二位数为3、4、5、6、7、8，后面再跟随机的9位数字
        self.regex = r'1[34578]\d{9}'

    #注意：修改转换过程中的值,默认父类BaseConverter中的方法是直接返回value
    def to_python(self, value):
        print("to_python方法被调用")
        # return "15911111111"
        return value

    def to_url(self, value):
        print("to_url方法被调用")
        return "18811111111"


# 2、将自己定义的转换器添加到flask应用中
app.url_map.converters["re_mobile"] = MobileConverter

# 3、 利用带有正则表达式的转换器发送短信
# 127.0.0.1:5000/send/18812345667
@app.route("/reseve/<re_mobile:mobile>")
def reseve_sms(mobile):
    return "The sms from %s" %(mobile)

@app.route("/home")
def home():
    url = url_for("reseve_sms",mobile='13855555555')
    return redirect(url)

if __name__ == '__main__':
    # 通过url_map函数可以查看整个flask的路由信息
    print(app.url_map)
    """启动flask程序"""
    app.run(debug=True)


