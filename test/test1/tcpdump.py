# -*- coding: utf-8 -*-
'''
@Author  : linhos
@Time    : 17-3-29 下午4:38
@Site    : 
@File    : tcpdump.py
@Software: PyCharm
'''
'''
python执行shell语句，将结果通过管道进行输出
暂时无法通过java直接调用shell命令，因为shell命令需要root权限
该方法仅仅是得到了print数据，还需要对数据进行切割，分解，存储
不同的数据，拥有不相同的数据格式，因此还需要对命令进行分解
'''
import sys
import subprocess
sub=subprocess.Popen('tcpdump -n -nn -vv -e -A',shell=True,stdout=subprocess.PIPE)
while sub.poll()==None:
    sys.stdout.flush()
    print sub.stdout.readline(),

print sub.returncode


