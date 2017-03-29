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
'''
import sys
import subprocess
sub=subprocess.Popen('tcpdump -n -nn -vv -XX -e -A',shell=True,stdout=subprocess.PIPE)
while sub.poll()==None:
    sys.stdout.flush()
    print sub.stdout.readline(),
print sub.returncode


