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

#onlyfiles = [f for f in listdir(all_html) if isfile(join(all_html, f))]

list_filename = []
for root, dirs, files in os.walk("../all_html/"):  
    for filename in files:
	list_filename.append(filename)


#print (list_filename)
#print (len(list_filename))

new_table = pd.DataFrame(columns=range(0,7), index = [0])
#new_table = pd.DataFrame(np.random.randint(size=(len(list_filename), 7)), columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_marker = 0;
list1 = []
for i in range(len(list_filename)):
	quote_page = 'file:///home/user/all_html/' + list_filename[i]
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	table = soup.find_all('table')[3] 
	#print (table)
	#new_table = pd.DataFrame(columns=range(0,7), index = [0])
	list1.append([])
	print (i)	
	for row in table.find_all('tr'):
		column_marker = 0
		columns = row.find_all('td')
		for column in columns:
			list1[row_marker].append(column.get_text())
			#new_table.iat[row_marker,column_marker] = column.get_text()
			column_marker += 1
	row_marker += 1

print(new_table)
