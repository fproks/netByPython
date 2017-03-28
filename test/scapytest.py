# -*- coding:utf8 -*-
import socket, time, thread

lock=thread.allocate_lock()

def socket_port(ip,port):
    #print("ip:%s"%ip)
    #print("port:%d"%port)
    try:
        if port >=65535:
            pass
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result==0:
            lock.acquire()
            j=j+1
            print ip,":",port,"open"
            lock.release()
        s.close()
    except Exception,e:
        pass
        #print(e)
        #print("端口异常:%d"%port)
def start():
    try:
        print("开始扫描")
        start_time =time.time()
        global j
        j=0
        for i in range(0,65535):
            #thread.start_new_thread(socket_port,('192.68.4.119',int(i)))
            socket_port('192.68.4.103',int(i))
        print ("扫描完成，用时:%2.f"%(time.time()-start_time))
        print(j)
    except:
        print ("扫描出错")

if __name__=="__main__":
    start()
