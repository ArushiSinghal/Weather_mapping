#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
from pandas import DataFrame

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

list_filename = []
for root, dirs, files in os.walk("../all_html/"):  
    for filename in files:
	list_filename.append(filename)

new_table = pd.DataFrame(columns=range(0,7), index = [0])
row_marker = 0
list1 = []
list_final = []
marking = 0;
for i in range(len(list_filename)):
	list_final.append([])
	quote_page = 'file:///home/user/all_html/' + list_filename[i]
	continent = list_filename[i]
	continent = continent.split('_')[0]
	print (continent)
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'lxml') 
	table = soup.find_all('table')[3] 
	row_marker = 0
	list1 = []
	for row in table.find_all('tr'):
		if (row_marker >= 3):
			break
		column_marker = 0
		columns = row.find_all('td')
		list1.append([])
		for column in columns:
			if (column_marker >= 2):
				break
			list1[row_marker].append(column.get_text())
			if (row_marker >= 1 and column_marker >= 1):
				list_final[marking].append(column.get_text())
			column_marker += 1
		row_marker += 1
	list_final[marking].append(continent)
	words2 = list_filename[i].split(".")
	words2 = words2[len(words2) - 1]
	list_final[marking].append(words2)
	marking += 1

list_final = pd.DataFrame(list_final)
print (list_final)
list_final.to_csv('a3.csv', sep='\t')
list_final.to_csv('a4.csv', sep='\t', encoding='utf-8')
