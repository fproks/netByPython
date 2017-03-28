# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-27 下午1:59
@Site    : 
@File    : Arp.py
@Software: PyCharm
'''

from StaticTools import *
class Arp:
    def __init__(self,directIP):
        self.__gateWayIp= NetTools.getGateway_ip()  #网关ip
        self.__directIp=directIP     #目标ip
        self.__selfIp=NetTools.get_ip_address()
