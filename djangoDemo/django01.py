# @Author : wangxz
# -*- coding: utf-8 -*-

a = [1, 2, 3]
b = a
b.append(4)
# 请问a的值是多少？如何把a拷贝给b（说出两种方式，并说出为什么），而不是共享一块内存。
print(id(a), id(b))

