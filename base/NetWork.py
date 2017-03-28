# -*- coding:utf8 -*-

'''
通过scapy ARP探测的方式对局域网络进行扫描 得到局域网了的IP地址和MAC地址
'''
import logging
import os
from scapy.all import srp,Ether,ARP,Conf
import socket
'''
logging.basicConfig(level=logging.ERROR,
                    filename='./log/log.txt',
                    filemode='w+',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
'''


def get_host_name(ip):
    host_name_list=os.popen('nbtscan -e '+ip).readlines()
    if len(host_name_list)==0:
        return None
    else:
        return host_name_list[0].split('\t')[1].split()[0]

def scanner_internet(ipscan):
    try:
        ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan),timeout=2,verbose=False)
    except Exception,e:
        logging.ERROR(e.message)
    else:
        print(type(ans[0][0]))
        for snd,rcv in ans:
            list_mac=rcv.sprintf("%Ether.src%  %ARP.psrc%")
            ip=rcv.sprintf("%ARP.psrc%")

            #name=socket.gethostbyaddr(ip)[0]

            print (list_mac)
            #print (rcv.sprintf("%Ether.src%"))   #mac地址
    logger=logging.getLogger("root")
    logger.error("get mac finished")
    logger.info("just test")


