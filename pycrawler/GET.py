import requests
import chardet
import Header_pool
import os
from urllib.request import urlopen
from tqdm import tqdm
import time
import IP_run
import Cookier

def get_Cr():
    global cookie 
    try:
        Cookier.run(url)
    except IndexError:
        print("Cookie is $#@#$")
        Cookier.StringCookier = ''
    cookie = Cookier.StringCookier
def HTML_get(url):
    Header_pool.give()
    headers = {
    'User-Agent':Header_pool.header
    }
    html = requests.get(url,headers)
    #用chardet进行内容分析
    CH1 = chardet.detect(html.content)
    BM = CH1['encoding']
    html.encoding = BM
    global StringHTML
    StringHTML = html.text
    global ContentHTML
    ContentHTML = html.content

def Download(url_file):
    filename = os.path.basename(url_file)
    IP_run.make()
    path = './Downloads\\'+filename
    Header_pool.give()
    headers = {
    'User-Agent':Header_pool.header
    }
    file_size = int(urlopen(url_file).info().get('Content-Length', -1))
    file_size /= 8192
    i = 0.0
    RB = requests.get(url_file,headers=headers,proxies=IP_run.proxy,stream=True)
    chunk_size = 10240
    count = 0
    fl = open(path,'wb')
    for data in RB.iter_content(chunk_size=chunk_size):
        count += 1
        current = len(data) * count / 1024 / 1024
        fl.write(data)
        fsize = os.path.getsize(path)
        fsize /= 8192
        i = ((fsize/file_size)*100)//1+1
        if int(i) <= 100:
            p = "working-[%s%s]%s%%-@%s-%skb/%skb" %('#'*int(i),' '*(100-int(i)),str((fsize/file_size)*100),str(current),str(fsize//1+1),str(file_size//1+1))
            print(p,end='\r')
    fl.close()
