import requests
import chardet
import Header_pool
import os
from urllib.request import urlopen
from tqdm import tqdm
import time
import IP_run
import Cookier

def get_Cr(url):
    global cookie 
    try:
        Cookier.run(url)
    except IndexError:
        print("Cookie is $#@#$")
        Cookier.StringCookier = ''
    cookie = Cookier.StringCookier
def HTML_post(url,json):
    Header_pool.give()
    get_Cr(url)
    headers = {
    'User-Agent':Header_pool.header,
    'cookie':cookie
    }
    html = requests.post(url,headers,json)
    #用chardet进行内容分析
    CH1 = chardet.detect(html.content)
    BM = CH1['encoding']
    html.encoding = BM
    global StringHTML
    StringHTML = html.text
    global ContentHTML
    ContentHTML = html.content

def POST_Download(url_file):
    filename = os.path.basename(url_file)
    IP_run.make()
    path = './Downloads\\'+filename
    Header_pool.give()
    get_Cr(url)
    headers = {
    'User-Agent':Header_pool.header,
    'cookie':cookie
    }
    file_size = int(urlopen(url_file).info().get('Content-Length', -1))
    file_size /= 8192
    i = 0.0
    RB = requests.post(url_file,headers=headers,proxies=IP_run.proxy,stream=True)
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
def File_post(url,FilePath):
    Header_pool.give()
    get_Cr(url)
    headers = {
    'User-Agent':Header_pool.header,
    'cookie':cookie
    }
    files = {
        'file':open(FilePath,'rb')
    }
    RB = requests.post(url,files=files)
File_post(url='https://postimages.org/',FilePath='./Downloads\\27fd3bbe55d439dd2026515227a4c8a735442123.jpg@518w_1e_1c.jpg')