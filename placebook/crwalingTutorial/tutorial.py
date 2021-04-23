#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
n = 0
f = open("/Users/daraelee/placebook-server/naver.txt", 'w')
with urlopen('https://www.naver.com') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("a.thumb"):
        n += 1
        data = anchor.img['alt'] + ': '+ anchor.img['src'] + "\n"
        print(anchor)
        f.write(data)
        f.close
