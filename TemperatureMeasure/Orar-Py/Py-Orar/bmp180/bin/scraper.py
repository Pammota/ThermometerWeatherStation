import requests
import unidecode
from bs4 import BeautifulSoup
from bs4 import Comment
import time

url = "https://www.vremea.ro/cluj/clujnapoca/"

def getVreme():
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    result = soup.find("p", {"class":"txtnow"})

    raw = result.text
    noacc=unidecode.unidecode(raw)

    number = noacc.find('\n') 

    return noacc[:number]

def getTemp():
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    result = soup.find("p", {"class":"txtnow"})

    lis = result.find_all('b')

    raw = lis[0].text
    noacc=unidecode.unidecode(raw)

    number = noacc.rpartition('d')[0]

    return number


def writerr(word):
    f = open("vreme.txt","w")
    f.write(word)
    f.close()

while 1:
    # vreme = getVreme()
    # writerr(vreme)
    # print(f"Running... {vreme} ...")
    print(getTemp())
    time.sleep(5)



