#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests

# specify the url
thislist = ['https://energyplus.net/weather-region/africa_wmo_region_1', 'https://energyplus.net/weather-region/asia_wmo_region_2', 'https://energyplus.net/weather-region/south_america_wmo_region_3', 'https://energyplus.net/weather-region/north_and_central_america_wmo_region_4', 'https://energyplus.net/weather-region/southwest_pacific_wmo_region_5', 'https://energyplus.net/weather-region/europe_wmo_region_6']

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

list_p = []

for j in range(6):
    print (j)
    print (thislist[j])
    req = urllib2.Request(thislist[j], headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    for div in soup.findAll('div', {'class': 'btn-group-vertical'}):
        aa = div.findAll('a')
        i = 0
        for aaa in aa:
            aaaa = aa[i]
            ss = "https://energyplus.net" + aaaa.attrs['href']
            print (ss)
            list_p.append(ss)
            print aaaa.text.strip(), '=>', aaaa.attrs['href']
            i += 1
list_pf = []
list_name = []
for k in range(len(list_p)):
    req = urllib2.Request(list_p[k], headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    for div in soup.findAll('div', {'class': 'btn-group-vertical'}):
        aa = div.findAll('a')
        i = 0
        for aaa in aa:
            aaaaa = aa[i]
            aaaa = aaaaa.attrs['href']
            ss = "https://energyplus.net" + "/weather-download" + aaaa[17:]
            pp = ss.rsplit('//',1)[1]
            ss = ss + "/" + pp + ".epw"
            sss = pp + ".epw"
            print (ss)
            list_pf.append(ss)
            list_name.append(sss)
            print aaaaa.text.strip(), '=>', aaaaa.attrs['href']
            i += 1

for k in range(len(list_pf)):
    print (list_pf[k])

print (list_pf)
for k in range(len(list_pf)):
    url = list_pf[k]
    print (url)
    r = requests.get(url, allow_redirects=True)
    open(list_name[k], 'wb').write(r.content)

print (len(list_pf))
