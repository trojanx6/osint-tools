import os
requmen = ["pip install requests ", "pip install bs4", "pip install colorama"]
for i in requmen:
    os.system(i)
os.system("clear")


from bs4 import BeautifulSoup as btu
import requests as req
from colorama import Fore, Style


class colors:
    Red = Fore.RED + Style.BRIGHT #kirmizi
    Gren = Fore.GREEN + Style.BRIGHT #yesil
    blue= Fore.BLUE + Style.BRIGHT # mavi
    yellow= Fore.YELLOW + Style.BRIGHT 
    magenta = Fore.MAGENTA + Style.BRIGHT # mor
    cyan = Fore.CYAN + Style.BRIGHT # acik mavi
    white = Fore.WHITE + Style.BRIGHT # beyaz
    
    
print(Fore.WHITE+ Style.BRIGHT +"""
#########                                    
    #    #    # # ##### ##### ###### #####  
    #    #    # #   #     #   #      #    # 
    #    #    # #   #     #   #####  #    # 
    #    # ## # #   #     #   #      #####  
    #    ##  ## #   #     #   #      #   #  
    #    #    # #   #     #   ###### #    # 
                                            
Twwitter Osint Tool
coder:Naci
"""+Fore.WHITE)


username = input(colors.Gren+"user name twiter: ")


class Main:
    def __init__(self):
        self.url =f"https://nitter.net/{username}/"
    def KaziKurek(self):
        istek = req.get(self.url)
        html = istek.text
        soup = btu(html, "html.parser")
        user = soup.find("a", {"class":"profile-card-fullname"}).text
        tweets_num = soup.find("span",{"class":"profile-stat-num"}).text
        following = soup.find("li",{"class":"following"}).find("span",{"class":"profile-stat-num"}).text
        followers = soup.find("li",{"class":"followers"}).find("span",{"class":"profile-stat-num"}).text
        likes = soup.find("li",{"class":"likes"}).find("span",{"class":"profile-stat-num"}).text
        img = soup.find("div",{"class":"profile-card"}).find("div",{"class":"profile-card-info"}).find("a", {"class":"profile-card-avatar"}).get("href")
        imglink = "https://nitter.net"+img#
        print(Fore.GREEN+ Style.BRIGHT + "User:"+Fore.WHITE+user)
        print(Fore.GREEN+ Style.BRIGHT + "following:"+Fore.WHITE+following)
        print(Fore.GREEN + Style.BRIGHT + "follwers:"+Fore.WHITE+followers)
        print(Fore.GREEN + Style.BRIGHT + "likes:"+Fore.WHITE+likes)
        print(Fore.GREEN+ Style.BRIGHT + 'Tweets Num:'+Fore.WHITE+tweets_num)
        print(Fore.GREEN+ Style.BRIGHT + 'Prodfile Img:'+Fore.WHITE+imglink)
        
if __name__=="__main__":
    app = Main()
    app.KaziKurek()