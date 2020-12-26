
import IP_test
import random
import re

IP = []
PORT = []
HTTP = []
proxy = {}

def Finder():
    print("输入代理区域/IP/类型/匿名类型/端口")
    while True:
        C = input("{Finder}[输入查找内容]{>>>}")
        f = open('IP_NEW_pool.txt','r',encoding='utf-8')
        c = C.replace('[NEW]','')
        for x in f:
            if c in x:
                x = x.replace('\n','')
                print(x)
    f.close()
def make1():
    C = input("{Finder}[输入IP区域]{>>>}")
    f = open('IP_NEW_pool.txt','r',encoding='utf-8')
    c = C.replace('[NEW]','')
    for x in f:
        if c in x:
            x = x.replace('\n','')
            print(x)
            IP1 = re.findall(r'(\d+\.\d+\.\d+\.\d+)',str(x))
            IP2 = re.findall(r'PORT:(.+?) 类',str(x))
            #IP:118.212.104.134 PORT:9999 类型:HTTP 位置:江西省新余市  联通 最后验证时间:2020-06-16 16:31:01
            IP3 = re.findall(r'类型:(.+?) 位',str(x))
            for y,z,a in zip(IP1,IP2,IP3):
                IP.append(y)
                PORT.append(z)
                HTTP.append(a)
    i = random.randint(1,len(IP))
    x = IP_test.IP[i]
    y = IP_test.PORT[i]
    z = IP_test.HTTP[i]
    proxy = {z:"http://"+x+":"+y}
    f.close()
def make():
    IP_test.get_IP()
    i = random.randint(1,len(IP_test.IP))
    x = IP_test.IP[i]
    y = IP_test.PORT[i]
    z = IP_test.HTTP[i]
    proxy = {z:"http://"+x+":"+y}
def make2(C):
    if C == None:
        C = input("{Finder}[输入IP的识别码{>>>}")
    else:
        C = C
    f = open('IP_pool.txt','r',encoding='utf-8')
    for x in f:
        a = re.findall(r'\[(\d+?)\]',x)
        for y in a:
            y = str(y)
            if str(C) in y:
                x = x.replace('\n','')
                print(x)
                IP1 = re.findall(r'(\d+\.\d+\.\d+\.\d+)',str(x))
                IP2 = re.findall(r'PORT:(.+?)-',str(x))
                #IP:118.212.104.134 PORT:9999 类型:HTTP 位置:江西省新余市  联通 最后验证时间:2020-06-16 16:31:01
                IP3 = re.findall(r'\[HTTP/HTTPS\]:(.+?)}',str(x))
                for y,z,a in zip(IP1,IP2,IP3):
                    IP.append(y)
                    PORT.append(z)
                    HTTP.append(a)
    x = IP[0]
    y = PORT[0]
    z = HTTP[0]
    proxy = {z:"http://"+x+":"+y}
    print(proxy)
    f.close()
def main():
    while True:
        i = input("{IP}{>>>}")
        if i == "/IP -get":
            import IP_get
            IP_get.IP_get_main()
        elif i == "/IP -test":
            IP_test.IP_test_main()
        elif i == "/IP -find":
            Finder()
        elif i == '/stop':
            break
