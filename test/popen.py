# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-24 下午3:22
@Site    : 
@File    : popen.py
@Software: PyCharm
'''
import os
import re
ip='192.68.4.101'
t =os.popen('nbtscan -e '+ip).readlines()
print(len(t))
print(t)
for l in t:
    t1=l.split('\t')[1].split()[0]
    print(t1)
