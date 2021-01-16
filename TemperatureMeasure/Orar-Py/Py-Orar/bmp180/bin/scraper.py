import requests
import unidecode
from bs4 import BeautifulSoup
from bs4 import Comment
import time

url = "https://www.vremea.ro/cluj/clujnapoca/"

def getvreme():
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    result = soup.find("p", {"class":"txtnow"})

    raw = result.text
    noacc=unidecode.unidecode(raw)

    number = noacc.find('\n') 

    return noacc[:number]

def writerr(word):
    f = open("vreme.txt","w")
    f.write(word)
    f.close()

while 1:
    vreme = getvreme()
    writerr(vreme)
    print(f"Running... {vreme} ...")
    time.sleep(350)



