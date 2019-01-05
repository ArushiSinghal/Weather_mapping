#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}


list_filename = []
for root, dirs, files in os.walk("../all_html/"):  
    for filename in files:
	list_filename.append(filename)


new_table = pd.DataFrame(columns=range(0,7), index = [0])
list1 = []
#for i in range(7):
for i in range(len(list_filename)):
	quote_page = 'file:///home/user/all_html/' + list_filename[i]
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	table = soup.find_all('p')[4] 
	ppp = table.get_text()
	ppp = ppp.split('WMO#=')[1]
	#print (ppp)
	list1.append([])
	list1[i].append(ppp)
	list1[i].append(list_filename[i])

print (list1)
