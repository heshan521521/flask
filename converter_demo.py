#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : converter_mini_demo.py.py
# @Author: heshan
# @Date  : 2020/3/15
# @Desc  : 自定义一个万能的转换器

from flask import Flask,url_for,redirect
from werkzeug.routing import BaseConverter

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
#转换器
# 127.0.0.1:5000/goods/123
# @app.route("/goods/<float:money>")
# @app.route("/goods/<path:goods_path>")
# @app.route("/goods/<goods_id>") #如果不加转换器类型，默认为字符串规则（除了/以外）
@app.route("/goods/<int:goods_id>")
def goods_details(goods_id): #添加传入参数goods_id
    """定义视图函数"""
    return "goods details page:  price is %d" %(goods_id)

# 1、自定义一个万能的转换器
class Regexconverter(BaseConverter):
    def __init__(self, url_map,regex):
        # 调用父类的初始化方法
        super(Regexconverter,self).__init__(url_map)
        # 将正则表达式的参数保存到对象中，然后flask会使用这个属性进行正则匹配
        self.regex = regex

# 2、将自己定义的转换器添加到flask应用中
app.url_map.converters["re"] = Regexconverter

# 3、利用带有正则表达式的转换器发送短信
# 127.0.0.1:5000/send/18812345667
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>") #正则表达式：r'1[34578]\d{9}'，表示1开头，且第二位数为3、4、5、6、7、8，后面再跟随机的9位数字
def send_sms(mobile):
    return "send sms to %s" %(mobile)


if __name__ == '__main__':
    # 通过url_map函数可以查看整个flask的路由信息
    print(app.url_map)
    """启动flask程序"""
    app.run(debug=True)


