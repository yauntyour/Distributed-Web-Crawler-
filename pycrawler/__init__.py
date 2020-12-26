import api
class redstone:
    def __init__(self,url=None,mode=None,json=None,FilePath=None,C=str):
        self.url = url
        self.mode = mode
        self.json = json
        self.FilePath = FilePath
        self.C = C
        return url
    def POST(self):
        api.post(url=self.url,mode=self.mode,json=self.json,FilePath=self.FilePath)
    def GET(self):
        api.get(url=self.url,mode=self.mode)
    def COOKIE(self):
        api.cookie()
    def COOKIES(seld):
        api.cookies(self.url)
    def IP(self):
        api.IP()
    def makeIP():
        api.IP_make(mode=self.mode,C=self.C)