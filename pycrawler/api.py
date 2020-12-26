import Cookier
import GET
import POST
import IP_run
import Header_pool
def cookies(url):
    Error = []
    try:
        if url = None:
            print("The url parameter cannot be empty")
        elif url = '':
            print("HTTP(S)Error:url is not had!")
        elif mode == None:
            print("The mode parameter cannot be empty")
        elif mode == '':
            print("The mode parameter cannot be empty")
        else:
            Cookier.run(url)
    except Exception as e:
        Error.append(e)
    if e != None:
        for e in Error:
            print(e)
def cookie():
    Error = []
    try:
        Cookier.main()
    except Exception as e:
        Error.append(e)
    if e != None:
        for e in Error:
            print(e)
def get(url=None,mode=None):
    Error = []
    try:
        if url = None:
            print("The url parameter cannot be empty")
        elif url = '':
            print("HTTP(S)Error:url is not had!")
        elif mode == None:
            print("The mode parameter cannot be empty")
        elif mode == '':
            print("The mode parameter cannot be empty")
        else:
            if mode == 'g':
                GET.HTML_get(url)
            elif mode == 'd':
                GET.Download(url)
    except Exception as e:
            Error.append(e)
    if e != None:
        for e in Error:
            print(e)
def post(url=None,mode=None,json=None,FilePath=None):
    Error = []
    try:
        if url = None:
            print("The url parameter cannot be empty")
        elif url = '':
            print("HTTP(S)Error:url is not had!")
        elif mode == None:
            print("The mode parameter cannot be empty")
        elif mode == '':
            print("The mode parameter cannot be empty")
        else:
            if mode == 'pg':
                if json == None:
                    json = ''
                    POST.HTML_post(url,json)
                else:
                    POST.HTML_post(url,json)
            elif mode == 'pd':
                POST.POST_Download(url)
            elif mode == 'pf':
                if FilePath == None:
                    print("Flie is null!! please put a filepath!!")
                else
                    POST.File_post(url,FilePath)
    except Exception as e:
            Error.append(e)
    if e != None:
        for e in Error:
            print(e)
#"制作者在这里留了一堆Bug，以后有时间在修吧~"
def IP():
    Error = []
    try:
        IP_run.main()
    except Exception as e:
            Error.append(e)
    if e != None:
        for e in Error:
            print(e)
def IP_make(mode=None,C=None):
    Error = []
    try:
        if mode == None:
            if C == None:
                IP_run.make()
            elif C != None:
                IP_run.make2(C)
        elif mode == 'f':
            IP_run.make1()
    except Exception as e:
            Error.append(e)
    if e != None:
        for e in Error:
            print(e)