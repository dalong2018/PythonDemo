# @Author : wangxz
# -*- coding: utf-8 -*-

class data():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex

    def get_name(self):
        str = "你的名字是"+self.name
        return str

    def get_age(self):
        str = "你的年龄是%d"%self.age
        return str

    def get_sex(self):
        str = "你的性别是"+self.sex
        return str

name = "wangzhe"
age = 18
sex = "男"
print(data(name,age,sex).get_name().upper())
print(data(name,age,sex).get_age())
print(data(name,age,sex).get_sex())

