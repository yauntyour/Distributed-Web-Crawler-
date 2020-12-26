from urllib import request
from http import cookiejar

def ROOT(StringCookie):
    f = open('Cookier_pool.txt','a')
    f2 = open('Cookier_pool.txt','r')
    t = True
    for x in f2:
        x = str(x)
        x = x.replace('\n','')
        if x == StringCookie:
            t = False
            print("This Cookie was had!")
            break
    if t == True:
        print("This Cookie wasn't had!")
        print(StringCookie)
        f.write(StringCookie+'\n')
    f.close()
    f2.close()

def Input():
    print("添加Cookie")
    print("格式为{网站名称}[URL]")
    s = input("{Cookier}{URL}")
    i = input("{Cookier}{输入Cookie}")
    StringCookie = "{**}["+s+"]"+"{%s}"%i
    ROOT(StringCookie)

def cookie(url):
    print("{游客Cookie爬取}")
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    response = opener.open(url)
    for item in cookie:
        StringCookie = "["+url+"]"+"{"+item.name+":"+item.value+"}"
        ROOT(StringCookie)