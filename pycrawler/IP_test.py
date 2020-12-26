import Header_pool
import requests
import re
import threading
import time

IP = []
PORT = []
HTTP = []
Header_pool.give()
url="http://icanhazip.com"
headers = {'User-Agent':Header_pool.header}

FL = open('IP_text_ARM_pool.arm','w')
FL.write('')
FL.close()

def one():
    f = open('IP_NEW_pool.txt','r',encoding='utf-8')
    F = open('IP_text_ARM_pool.arm','a',encoding='utf-8')
    for x in f:
        F.write(x)
    F.close()
    f.close()
def get_IP():
    one()
    Fl = open('IP_text_ARM_pool.arm','r',encoding='utf-8')
    for x in Fl:
        x = x.replace('\n','')
        IP1 = re.findall(r'(\d+\.\d+\.\d+\.\d+)',str(x))
        IP2 = re.findall(r'PORT:(.+?) 类',str(x))
        IP3 = re.findall(r'类型:(.+?) 位',str(x))
        for y,z,a in zip(IP1,IP2,IP3):
            IP.append(y)
            PORT.append(z)
            HTTP.append(a)
    Fl.close()
def TEST(i,x,y,z):
    FIP = open('IP_pool.txt','a')
    proxy = {
        z:"http://"+x+":"+y
    }
    html = requests.get(url,headers,proxies=proxy,timeout=5)
    Get_IP = re.findall(r'(\d+\.\d+\.\d+\.\d+)',str(html.text))
    print("IP.NO."+str(i)+"值为"+str(Get_IP))
    for a in Get_IP:
        if a == x:
            FIP.write(String_IP)
        else:
            print("This IP-"+str(proxy)+"can't use")
    FIP.close()
def IP_test_main():
        get_IP()
        i = 0
        Thread = []
        while True:
                i+=1
                t1 = threading.Thread(target=TEST(i,x=IP[i],y=PORT[i],z=HTTP[i]))
                Thread.append(t1)
                if i == len(IP):
                    break
        for t1 in Thread:
            print("Thread{%d}[ON]"%i)
            t1.start()
        FL = open('IP_text_ARM_pool.arm','w')
        FL.write('')
        FL.close()