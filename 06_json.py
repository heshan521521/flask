#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : json 的用法


from flask import Flask,json,jsonify

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/index')
def index():
    """json是一个字典"""
    data = {
        "name":"zhangsan",
        "age":18
    }
    # json.dumps(字典) 是将python的字典转换为json字符串
    # json.loads(字符串) 是将字符串转换为python中的字典

    # # 方法一：最原始的方法
    # json_str = json.dumps(data)
    # # return json_str
    # # 由于直接 return json_str的时候Content-Type: text/html;与我们传入的json类型不符，如有需要，可以将其改成json类型
    # return json_str, 200 ,{"Content-Type":"application/json"}

    # #方法二：jsonify帮我们转为json, 不需要自己对响应头做处理，Content-Type已经是application/json了
    # return jsonify(data)

    #jsonify可以传入参数，如：
    return jsonify(city = "hangzhou",country = "china")
if __name__ == '__main__':
    app.run(debug=True)
