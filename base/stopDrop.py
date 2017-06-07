# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-6-7 上午10:53
@Site    : 
@File    : stopDrop.py
@Software: PyCharm
'''

import os
import sys

def stopDrop(param):
    os.system("rmmod %s" %param)

if __name__ =="__main__":
    param =sys.argv[1]
    if param ==1:
        #stopDrop("drop")
        print "drop"
    if param ==2:
        print "alert"
    exit(0)