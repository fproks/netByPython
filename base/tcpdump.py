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
import signal

def tcpdump(host):
    sub=subprocess.Popen('tcpdump src host '+host+' -n -nn -vv -e -A',shell=True,stdout=subprocess.PIPE)
    try:
        while sub.poll()==None:
            sys.stdout.flush()
            print sub.stdout.readline()

        print sub.returncode
    except:
        sub.kill()
        exit(0)

if __name__ =="__main__":
    #host=sys.argv[1]
    host="192.68.4.103"
    #print host
    tcpdump(host)
    exit(0)

