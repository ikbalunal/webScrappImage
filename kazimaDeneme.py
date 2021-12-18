import os
import urllib.request
import requests
from bs4 import BeautifulSoup

#klasik bs4 işlemleri
r = requests.get("https://en.wikipedia.org/wiki/Diatom")
soup = BeautifulSoup(r.content, 'lxml')

links_array = []

#hedeflediğim content'ten img src yi scrap ediyorum
uls = soup.find_all('ul', {'class': 'gallery mw-gallery-packed'})
for ul in uls:
    for li in ul.find_all('li'):
        for link in li.find_all('a'):
            for image1 in link.findAll('img'):
                links_array.append("http:" + image1['src'])

# fotograflar dosyası yoksa oluştur (dizine)
if not os.path.exists("fotograflar"):
    os.makedirs("fotograflar")
# Linkleri Yazdırıyorum (check:value)
for siraLink in links_array:
    print(siraLink)


SAVE_FOLDER = "C:/Users/USER/Desktop/Python/htmlParser/fotograflar"
sayac1=0

# Linklerin bulunduğu dizide dolaşarak, resimleri indiriyorum
for imagelink in links_array:
    response = requests.get(imagelink)
    sayac1=sayac1+1
    imageName = SAVE_FOLDER + '/' + "diatomFoto" + str(sayac1 + 1) + '.jpg' # resimi adlandırma
    with open(imageName, 'wb') as file:
        file.write(response.content)
