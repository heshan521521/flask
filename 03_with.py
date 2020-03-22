#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File  : 01_request.py
# @Author: heshan
# @Date  : 2020/3/22
# @Desc  : with 的用法

# # 文件操作方法
# f = open("./1.py","w")
# try :
#     f.write("hello flask !")
# except Exception:
#     pass
# finally:
#     f.close()

# # 使用with方式实现
# with open("./1.txt" , "w") as f:
#     f.write("hello flask !! ")
#     f.write("hello flask !! ")
#     f.write("hello flask !! ")
#     f.write("hello flask !! ")

class Foo(object):
    def __enter__(self):
        """进入with 语句的时候被with调用"""
        print("enter called!")
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出with 的时候被with调用 """
        print("exit called")
        print("exc_type is %s" %exc_type)
        print("exc_val is %s" %exc_val)
        print("exc_tb is %s" %exc_tb)

with Foo() as foo:
    print("hello with")

    #手动制造异常
    a = 1 / 0
    print("hello end")
