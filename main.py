#
# TODO: 1. proxy
#       2. diff user-agents
#       3. server
#       4. table on g disc 
#

import requests
import time
from bs4 import BeautifulSoup
import random

#
# Func to move to follow the link
#

def make_request(url):

    """headers_list = [{'user-agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15'},
                    {'user-agent' : 'Mozilla/5.0 (iPhone13,3; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1 '},
                    {'user-agent' : 'Mozilla/5.0 (Linux; Android 9; KFTRWI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Safari/537.36'},
                    {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'},
                    {'user-agent' : 'Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'},
                    {'user-agent' : 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/92.0.4515.119 Safari/537.36'},
                    {'user-agent' : 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) '},
                    {'user-agent' : 'Mozilla/5.0 (Applxe Watch5,9; CPU Apple Watch WatchOS like Mac OS X; WatchApp'},
                    {'user-agent' : 'Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343'},
                    {'user-agent' : 'RokuOS/3.0.0|Roku 3930X|STB|RokuOS 9.4.0 4200 '}
                    ]
                    
    headers = random.choice(headers_list)
    print(headers)"""
    
    headers = {'user-agent' : 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/92.0.4515.119 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    time.sleep(3)
    print('====================================================================================================================================================')
    print(soup)
    print('====================================================================================================================================================')

    return(soup)

#
# Func to collect types of products
# and links to them
#
# types = [[list of types], [list of links]]
#

def get_types(soup):
    types = [[], []]
    for ultag in soup.find_all('ul', {'class': 'tabs'}):
        for litag in ultag.find_all('li'):
            types[0].append(litag.text)
            for i in litag.find_all('a'):
                types[1].append(i['href'])
    return types

#
# Func to collect sizes of all types
# and links to them
#
# sizes = [[[sizes of 1 type], [links for sizes of 1t]], ...]
#

def get_size(res, url):
    sizes = [[], []]
    for div in res.find_all('div', {'class': 'panes'}):
        for a in div.find_all('a'):
            sizes[0].append(a.string)
            sizes[1].append(url + a['href'])
    return sizes

#
# Func to create full names of products
#
# name = type + size
#

def make_name(ty, sizes):
    names = []
    for size in sizes:
        names.append(ty + ' ' + size)
    return names  

#
# Func to collect costs of all types
# and sizes
#
# prices = [[[t1 s1], [t1 s2], [t1 s3]..], [[t2 s1], ...], ...] 
#

def get_cost(soup):
    prices = []
    for spantag in soup.find_all('span', {'class': 'cost'}):
        prices.append(spantag.text)
    return prices        

#
# Func to collect producers of all types
# and sizes
#
# prods = [[[t1 s1], [t1 s2], [t1 s3]..], [[t2 s1], ...], ...] 
#

def get_prod(soup):
    prods = []
    for atag in soup.find_all('a', {'class': 'firm_link'}):
        prods.append(atag.string)
    return prods        

#
# Func to create full data
#

def make_data(names, sizes, prods, prices):
    data = []
    print(names)
    print(sizes)
    print(prods)
    print(prices)
    for i in range(len(names)):
        for j in range(len(sizes[i])):
            for k in range(len(prods[i][j])):
                string = [names[i], sizes[i][0][j], 
                prices[i][j][k], prods[i][j][k]]
                data.append(string)
    return data

def main():
    url  = 'http://23met.ru/price'
    url1 = 'http://23met.ru' 

    soup   = make_request(url)
    types  = get_types(soup)
    names  = []
    sizes  = []
    prods  = []
    prices = []
    data   = []

    i = 0

    """for href in types[1]:
        soup = make_request(href)
        sizes += get_size(soup, url1)
        i += 1
        print(i)
    for i in range(len(types[0])):
        make_name(types[0][i], sizes[i][0])
    for ty in sizes:
        for href in ty[1]:
            soup = make_request(href)
            prods_i  += get_prod(soup)
            prices_i += get_cost(soup)
        prods.append(prods_i)
        prices.append(prices_i)

    # =======TESTING_CODE======== """

    soup_1 = make_request(types[1][0])
    sizes = get_size(soup_1, url1)
    names = make_name(types[0][0], sizes[0])
    soup_2 = make_request(sizes[1][1])
    print(2)
    soup_3 = make_request('http://23met.ru/price_nerzh')
    print(3)
    soup_4 = make_request(sizes[1][2])
    print(4)
    soup_5 = make_request('http://23met.ru/services')
    print(5)
    soup_6 = make_request(sizes[1][3])
    print(6)
    soup_7 = make_requests('http://23met.ru/robots.txt')
    print(7)
    soup_8 = make_request(sizes[1][4])
    print(8)
    soup_9 = make_request('http://23met.ru')
    print(9)
    soup_10 = make_request(sizes[1][5])
    print(10)
    
    prices = get_cost(soup_3)
    prods  = get_prod(soup_3)
    #print(prods)
    #print(prices)

if __name__ == '__main__':
    main()
