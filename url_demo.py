# coding:utf8
from flask import Flask,url_for,redirect

# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

#通过methods方法来设置访问方式
@app.route('/post_only',methods=["POST"])
def post_only():
    return "This is Post Page"

#假如两个路由地址相同，且请求方式也相同的时候，第一个会覆盖第二个。。但是如果请求方式不同，则是两个不同的
@app.route('/hello',methods=["POST"])
def hello():
    return "hello zhangshan"

@app.route('/hello',methods=["GET"])
def hello2():
    return "hello lisi"

@app.route('/index')
@app.route('/home')
def home_page():
    return "Welcome to My Blog"

@app.route('/login')
def login():
    # 使用url_for函数，通过视图函数的名称找到对应的视图的url路径
    url = url_for('index')
    return redirect(url)

# 使用Url_for函数反解析的好处在于，如果被跳转的页面改动了，底下的代码无需改动，可以随着变更。
@app.route('/register')
def register():
    url = url_for('index')
    return redirect(url)

if __name__ == '__main__':
    # 通过url_map函数可以查看整个flask的路由信息
    print(app.url_map)
    """启动flask程序"""
    app.run(debug=True)


