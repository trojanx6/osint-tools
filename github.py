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
    Red = Fore.RED + Style.BRIGHT 
    Gren = Fore.GREEN + Style.BRIGHT 
    blue= Fore.BLUE + Style.BRIGHT 
    yellow= Fore.YELLOW + Style.BRIGHT 
    magenta = Fore.MAGENTA + Style.BRIGHT 
    cyan = Fore.CYAN + Style.BRIGHT 
    white = Fore.WHITE + Style.BRIGHT 
    
    

print(colors.white+"""
 dP""b8 88 888888 88  88 88   88 88""Yb     
dP   `" 88   88   88  88 88   88 88__dP     
Yb  "88 88   88   888888 Y8   8P 88""Yb     
 YboodP 88   88   88  88 `YbodP' 88oodP
 
 Beta Sürüm 
 coder:Naci
""")
username = input(colors.blue+"user name: ")    
class UserScanGithub():
    def __init__(self):
        self.username = username
        self.urlGitHub = f"https://github.com/{username}"
        
    def GitHub(self):
        ListeGithub = []
        NewsRequestsGithub = req.get(self.urlGitHub)
        NewsHtmlGithub = NewsRequestsGithub.text
        NewsSoupGithub = btu(NewsHtmlGithub, "html.parser")
        try:
            NewsUserNameGithub = NewsSoupGithub.find_all("span",attrs={"class":"p-nickname vcard-username d-block"})
            NewsUserNameGithub= " ".join(gituser.text for igit in NewsUserNameGithub for gituser in igit.findAll(text=True)).strip()
            NewsNameGithub = NewsSoupGithub.find("span",{"class":"p-name vcard-fullname d-block overflow-hidden"}).text.strip()
            if NewsUserNameGithub == username:
               NewsImgGithub = NewsSoupGithub.find("div",{"class":"position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0"}).find("a").get("href")
               NewsBioGithub = NewsSoupGithub.find("div",{"class":"p-note user-profile-bio mb-3 js-user-profile-bio f4"}).text
               NewsFollowingGithub = NewsSoupGithub.find_all("span",{"class":"text-bold color-fg-default"})
               NewsFollowersGithub = NewsSoupGithub.find("a",{"class":"Link--secondary no-underline no-wrap"})
               for iFollowers in NewsFollowingGithub:
                   NewsListe = ListeGithub.append(iFollowers.text)
               NewsFollowersGithub = ListeGithub[0]
               NewsFollowingGithub = ListeGithub[1]
               NewsRepoGithub = NewsSoupGithub.find("span",{"class":"Counter"}).text
               NewsOutputGithub = f"""
{colors.white}User:{colors.Gren} {self.username}
{colors.white}Name:{colors.Gren} {NewsNameGithub}
{colors.white}Profil Avatar:{colors.Gren} {NewsImgGithub}
{colors.white}Following:{colors.Gren} {NewsFollowersGithub}
{colors.white}Followers:{colors.Gren} {NewsFollowingGithub}
{colors.white}Repositiois:{colors.Gren} {NewsRepoGithub}
{colors.white}Bio:{colors.Gren} {NewsBioGithub}
{colors.white}Link:{colors.Gren} {self.urlGitHub}"""
               print(NewsOutputGithub.strip())
            else:
                pass
        except:
                print(colors.Red+"Github Not Found !")
                
                
if __name__=="__main__":
    Scan = UserScanGithub()
    Scan.GitHub()