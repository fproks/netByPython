# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-20 上午9:52
@Site    : 
@File    : arptest.py
@Software: PyCharm
'''
import sys
sys.path.append('..')
from base.StaticTools import *
from base.NetWork import *
from scapy.all import ARP,send
dirIP='192.68.4.102'
NetTools.ARP_attract_with_Process(dirIP)
while 1:
    pass