#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : wtf表单 的用法


from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
#导入验证器的常用验证函数
from wtforms.validators import DataRequired,EqualTo


# 导入Flask类
# __name__表示当前的模块名称
# 模块名，flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

app.config["SECRET_KEY"] = "dsakkflasfklsafkd3i2kdsa"
#定义表单的模型类
class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    # 添加label表签 validators验证器,DataRequired验证数据是否为空
    user_name = StringField(label=u"用户名",validators=[DataRequired(u"用户名不能为空！")])
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码不能为空！ ")])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired(u"确认密码不能为空！ "),EqualTo("password",u"输入的两次密码不一致!")])

    submit = SubmitField(label=u"提交")

@app.route("/register",methods=["GET","POST"])
def register():
    """创建表单对象,
    如果是post请求，前端发送了数据，
    flask会把数据在构造form对象的时候存放到对象中
    """
    form = RegisterForm()

    #判断form表单中的数据是否合规
    #如果form表单中的数据完全验证无误，则返回真，否则返回假
    if form.validate_on_submit():
        #如果验证无误，则开始提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname,pwd,pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))

    return render_template("register.html",form = form)

@app.route("/index")
def index():
    user_name = session.get("user_name","")
    return "hello %s" %user_name

if __name__ == '__main__':
    app.run(debug=True)