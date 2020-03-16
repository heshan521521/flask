# coding:utf8
from flask import Flask , current_app

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/python",  #访问静态资源的url前缀,默认值为static
            static_folder="static",     #静态文件的目录，默认值为static
            template_folder="templates",#模板目录，默认值为templates
            )
# 配置参数的使用
# 1、使用配置文件
# app.config.from_pyfile("config.cfg")

# 2、使用对象的方式配置参数（通常使用的方式），
class Config(object):
   DEBUG = True
   """还可以自定义属性"""
   ITCAST = "python"
app.config.from_object(Config)

# 3、直接操作config字典对象
#app.config["DEBUG"]= True

# 4、直接放在记动程序参数中，如app.run(debug=True)

@app.route('/')
def index():
    # a = 1 / 0 # 人工制造错误，使错误在调试模式时暴露出来
    # 获取自定义配置参数
    # 1、直接从全局对象app.config字典中获取
    #print(app.config.get("ITCAST"))
    # 2、通过导入current_app包的获取参数
    print(current_app.config.get("ITCAST"))
    return 'Hello World!'


if __name__ == '__main__':
    """启动flask程序"""
    app.run()
    # app.run(host="192.168.31.251",port=8000)
    """如果host绑定为0.0.0.0，本机的所有IP地址均可访问,如：
        http://localhost:8000/
        http://192.168.31.251:8000/ #内网地址
        http://127.0.0.1:8000/
    """
    # app.run(host="0.0.0.0",port=8000,debug=True)

