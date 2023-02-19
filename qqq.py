import requests as req
from bs4 import BeautifulSoup as bs

class Main():
    def __init__(self):
        self.url = "https://www.turkhackteam.org/uye/adanlitrojan.950398/"
        self.xf_tf = "epskM-v-t1eTLdx1mgncp2cuUdcxbMoE"
        self.xf_user = "950398,jH-bukrd26e9RP6Fn6txcVsYvluFQpE6D6tK75nx"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        self.sayac = 0
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
        try:
            for s in range(0,11):
                istek = req.get(f"https://www.turkhackteam.org/arama/267966/?page={s}",headers=self.headers)
                html = istek.text
                soup = bs(html, "lxml")
                classListe = (soup.find_all("ul", class_="listInline listInline--bullet"))
                url = soup.find_all("h3", class_="contentRow-title")
                for link,forum in zip(url,classListe):
                    urls ="https://www.turkhackteam.org"+link.find("a").get("href")
                    date = forum.find("time").get("datetime").split("T")[0]
                    yer = forum.find_all("li")[-1].getText()
                    if yer == "Forum: THT Yardım Merkezi":
                        print(urls)

        except:
            pass





if __name__=="__main__":
    app = Main()
    app.log()
    app.scrping()

