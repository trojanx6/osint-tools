import os
requmen = ["pip install requests ", "pip install bs4", "pip install colorama"]
for i in requmen:
    os.system(i)
os.system("clear")
import requests as req
from bs4 import BeautifulSoup as btu
import random
from colorama import Fore, Style


class colors:
    Red = Fore.RED + Style.BRIGHT #kirmizi
    Gren = Fore.GREEN + Style.BRIGHT #yesil
    blue= Fore.BLUE + Style.BRIGHT # mavi
    yellow= Fore.YELLOW + Style.BRIGHT 
    magenta = Fore.MAGENTA + Style.BRIGHT # mor
    cyan = Fore.CYAN + Style.BRIGHT # acik mavi
    white = Fore.WHITE + Style.BRIGHT # beyaz
    
    
#xsugrantx

print(colors.white+"""
d8888b. d888888b d8b   db d888888b d88888b d8888b. d88888b .d8888. d888888b      
88  `8D   `88'   888o  88 `~~88~~' 88'     88  `8D 88'     88'  YP `~~88~~'      
88oodD'    88    88V8o 88    88    88ooooo 88oobY' 88ooooo `8bo.      88         
88~~~      88    88 V8o88    88    88~~~~~ 88`8b   88~~~~~   `Y8b.    88         
88        .88.   88  V888    88    88.     88 `88. 88.     db   8D    88         
88      Y888888P VP   V8P    YP    Y88888P 88   YD Y88888P `8888Y'    YP         
                                                                                 
                                                                                

Beta Sürüm 
coder:Naci                                                                                 
""")
username = input(colors.magenta+"user name: ")
ListePin = []
class UserScanPinterest:
    def __init__(self):
        self.urlPinter = f"https://tr.pinterest.com/{username}/"
        
    def Pinterest(self):
        NewsRequestsPin = req.get(self.urlPinter)
        NewsHtmlPin = NewsRequestsPin.text
        NewsSoupPin = btu(NewsHtmlPin, "html.parser")
        try:
            NewsNamePin = NewsSoupPin.find("div",{"class":"FNs zI7 iyn Hsu"}).text
            NewsUserNamePin = NewsSoupPin.find("span",{"class":"tBJ dyH iFc sAJ EdS zDA IZT swG"}).text
            NewsBioPin = NewsSoupPin.find("span",{"class":"tBJ dyH iFc sAJ O2T zDA IZT swG"}).text
            NewsFollowingPin = NewsSoupPin.find("div",{"class":"tBJ dyH iFc sAJ O2T zDA IZT H2s"}).text
            NewsImgPin = NewsSoupPin.find("img",{"class":"hCL kVc L4E MIw"}).get("src")
            NewsFollowersPin_ = NewsSoupPin.find_all("div",{"class":"tBJ dyH iFc sAJ O2T zDA IZT H2s"})
            for iPin in NewsFollowersPin_:
                ListePin.append(iPin.text)
            NewsFollowersPin = ListePin[0]
            NewsFollowingPin = ListePin[1]
            NewsPinSPin = NewsSoupPin.find("img",{"class":"hCL kVc L4E MIw"}).get("src")
            NewsOutPutPin = f"""
{colors.Gren}Name:{colors.white}{NewsNamePin}
{colors.Gren}Bio:{colors.white}{NewsBioPin}
{colors.Gren}Following:{colors.white}{NewsFollowingPin}
{colors.Gren}Followers:{colors.white}{NewsFollowersPin}
{colors.Gren}İmg:{colors.white}{NewsImgPin}
            """
            print(NewsOutPutPin)
        except:
            pass
        
        
        
        
if __name__=="__main__":
    app = UserScanPinterest()
    app.Pinterest()        