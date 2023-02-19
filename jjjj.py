import requests as req
from bs4 import BeautifulSoup as bs

class Main():
    def __init__(self):
        self.url = "https://www.turkhackteam.org/uye/adanlitrojan.950398/"
        self.xf_tf = "epskM-v-t1eTLdx1mgncp2cuUdcxbMoE"
        self.xf_user = "950398,jH-bukrd26e9RP6Fn6txcVsYvluFQpE6D6tK75nx"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        self.cookie = {
            'xf_user': f'{self.xf_user}',
            'xf_tfa_trust': f'{self.xf_tf}'
        }

    def log(self):
        login = req.get(self.url,cookies=self.cookie, headers=self.headers)
        control = "Giriş yap"
        html = login.text
        if control in html:
            print("giris yapılmadı")
        else:
            print("giris yapıldı")

    def scrping(self):
        for i in range(0,10):
            request = req.get(f"https://www.turkhackteam.org/arama/267966/?page={i}", headers=self.headers)
            html = request.text
            parser = bs(html,"html.parser")
            body = parser.find_all("ol",{"class":"block-body"})
            for div in body:
                mesaaj = div.find_all("div",{"class":"contentRow-main"})
                print(mesaaj)
https://www.turkhackteam.org/arama/267966
if __name__=="__main__":
    app = Main()
    app.log()
    app.scrping()

