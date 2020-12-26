import re
import random
import Cookie_get

Cookie = []
StringCookier = ''
def run(url):
    f = open('Cookier_pool.txt','r')
    for x in f:
        x = x.replace('\n','')
        a = re.findall(r'\[(h.+?)\]',str(x))
        for y in a:
            if y in url:
                Cookie.append(x)
            else:
                Cookie_get.cookie(url)
                break
    i = random.randint(0,len(Cookie))
    s = Cookie[i]
    b = re.findall(r'{(.+?)}',str(s))
    for z in b:
        StringCookier = str(z)
        print(StringCookier)
def main():
    while True:
        i = input("{Cookier}{>>>}")
        if i == "/input":
            Cookie_get.Input()
        elif i == "/cookie -get":
            url = input("{Cookier}{>>>}")
            Cookie_get.cookie(url)
        elif i == "/stop":
            break