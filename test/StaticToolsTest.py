# -*- coding:utf8 -*-
import sys,os
sys.path.append(os.path.dirname(__file__)+"/../")
#sys.path.expanduser('~/packet')
from base.StaticTools import *
from base.NetWork import *
import codecs
import  logging
import logging.config
#print (NetTools.getGateway_mac())


'''
    StaticTools 的启动函数,未来继续修改，可以直接使用StaticTools启动
'''

if __name__=="__main__":
    print(os.path.dirname(__file__))
    log_path=os.path.join(os.path.dirname(__file__)+"/../log/logconfig.ini")
    logging.config.fileConfig(codecs.open(log_path,'r','utf-8'))
    NetTools.getGateway_mac()
    local_work=NetTools.search_with_gateway()
    print (local_work)
    scanner_internet(local_work)

