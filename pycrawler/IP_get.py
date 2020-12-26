from bs4 import BeautifulSoup
import requests
import re
import Header_pool
import threading
import time

def IP_get(url):
        Header_pool.give()
        headers = {
        'User-Agent':Header_pool.header
        }
        html = requests.get(url,headers)
        soup = BeautifulSoup(html.content,'html5lib')
        p = soup.find_all('td')
        f = open('IP_NEW_pool.txt','a',encoding='utf-8')
        IP1 = re.findall(r'(\d+\.\d+\.\d+\.\d+)',str(p))
        IP2 = re.findall(r'PORT">(.+?)<',str(p))
        IP3 =  re.findall(r'类型">(.+?)<',str(p))
        IP4 = re.findall(r'位置">(.+?)<',str(p))
        IP5 = re.findall(r'最后验证时间">(.+?)<',str(p))
        for ip1,ip2,ip3,ip4,ip5 in zip(IP1,IP2,IP3,IP4,IP5):
                ip1 = str(ip1)
                ip2 = str(ip2)
                ip3 = str(ip3)
                ip4 = str(ip4)
                ip5 = str(ip5)
                f.write("IP:"+ip1+" PORT:"+ip2+" 类型:"+ip3+" 位置:"+ip4+" 最后验证时间:"+ip5+'\n')
                f.close()
def IP_get_main():
        i = 0
        while i <= 3561:
                i+=1
                url="https://www.kuaidaili.com/free/inha/%d/" % i
                t1 = threading.Thread(target=IP_get(url))
                time.sleep(0.001)
                print("Thread{%s}[ON]"%i)
                t1.start()