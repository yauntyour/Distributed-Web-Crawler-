import random

FindHeader = []
Header = []
header = ''

def give():
    f = open('Header_pool.txt','r')
    for x in f:
        x = x.replace('\n','')
        Header.append(x)
    z = random.randint(0,len(Header))
    try:
        header = Header[z]
    except:
        z = random.randint(0,len(Header)-1)
        header = Header[z]
def Give():
    f = open('Header_pool.txt','r')
    i = 0
    while True:
        C = input("{Header}{Find}")
        for x in f:
            i += 1
            x = x.replace('\n','')
            if C in x:
                FindHeader.append(x)
            elif '/stop' in C:
                break
def Writer():
    print("添加Header到Header_pool")
    while True:
        i = str(input("{Header}{>>>}"))
        with open('Header_pool.txt','a') as F:
            F.write(i+'\n')
        if i == '/stop':
            break