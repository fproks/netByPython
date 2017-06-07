# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-4-24 上午10:41
@Site    : 
@File    : readss.py
@Software: PyCharm
'''

ig =open("/home/linhos/progect/HTML/3/img/timg.svg",mode='r')
s=""
for i in ig.readlines():
    s=s+i[:-2]
print s