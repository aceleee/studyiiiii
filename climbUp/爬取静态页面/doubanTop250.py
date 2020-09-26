#!/usr/bin/pyrhon
# coding: utf-8

import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'orgin': 'https: // movie.douban.com'
    }
    name_list = []
    for i in range(0,10):
        link = "https://movie.douban.com/top250?start={}&filter=".format(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print("===", r.status_code)
        #print(r.text)
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')
        #print(div_list)
        for span in div_list:
            movie_name = span.a.span.text.strip()
            name_list.append(movie_name)
        #print(div_list)
    return name_list

movie = get_movies()
print(movie)