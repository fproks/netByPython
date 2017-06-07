# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-6-7 上午10:43
@Site    : 
@File    : startAlert.py
@Software: PyCharm
'''

import os
import sys

def startAlert(param):
    os.system("insmod /home/linhos/progect/Sping/ATTRACT/security/script/alert.ko")
    os.system(' echo "%s" >/proc/alert_proc' %param)

if __name__ =="__main__":
    param =sys.argv[1]
    startAlert(param)
    exit(0)
