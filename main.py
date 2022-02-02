#
# TODO: 1. proxy
#       2. diff user-agents
#       3. server
#       4. table on g disc 
#

import requests
import time
from bs4 import BeautifulSoup

def make_request(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    time.sleep(10)
    return(soup)

def get_types(soup):
    types = [[], []]
    for ultag in soup.find_all('ul', {'class': 'tabs'}):
        for litag in ultag.find_all('li'):
            types[0].append(litag.text)
            for i in litag.find_all('a'):
                types[1].append(i['href'])
    return types

def get_size(res, url):
    sizes = [[], []]
    for div in res.find_all('div', {'class': 'panes'}):
        for a in div.find_all('a'):
            sizes[0].append(a.string)
            sizes[1].append(url + a['href'])
    return sizes

def make_name(ty, sizes):
    names = []
    for size in sizes:
        names.append(ty + ' ' + size)
    return names  

def get_cost(soup):
    prices = []
    for spantag in soup.find_all('span', {'class': 'cost'}):
        prices.append(spantag.text)
    return prices        

def get_prod(soup):
    prods = []
    for atag in soup.find_all('a', {'class': 'firm_link'}):
        prods.append(atag.string)
    return prods        

def main():
    url  = 'http://23met.ru/price'
    url1 = 'http://23met.ru' 
    headers = {'user-agent': 'Mozilla/5.0'}

    soup = make_request(url)
    types = get_types(soup)
    names = []
    sizes = []
    #for href in types[1]:
    #    res = requests.get(href, headers = headers)
    #    sizes += get_size(res)
    #    time.sleep(10)
    #for i in range(len(types[0])):
    #    make_name(types[0][i], sizes[i][0])
    soup_1 = make_request(types[1][0])
    sizes = get_size(soup_1, url1)
    names = make_name(types[0][0], sizes[0])
    soup_2 = make_request(sizes[1][1])
    prices = get_cost(soup_2)
    prods  = get_prod(soup_2)
    print(prods)
    print(prices)

if __name__ == '__main__':
    main()
