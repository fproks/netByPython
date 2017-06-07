# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-6-7 上午9:01
@Site    : 
@File    : startDrop.py
@Software: PyCharm
'''
import os;
import sys
import subprocess

def startDrop():
    tmp =os.popen("ls").readlines()
    print tmp


if __name__ =="__main__":
    startDrop()
    exit(0)