# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-27 下午2:43
@Site    : 
@File    : test.py
@Software: PyCharm
'''
f=open('/proc/sys/net/ipv4/ip_forward','r')
p=f.readline()
print(p)
f.close()
f=open('/proc/sys/net/ipv4/ip_forward','wb')
f.write('0')
f.close()
f=open('/proc/sys/net/ipv4/ip_forward','r')
p=f.readline()
print(p)
f.close()

import socket
import fcntl
import struct

import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print(get_ip_address('eno1'))