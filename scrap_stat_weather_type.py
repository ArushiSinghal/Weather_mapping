#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

list_filename = []
for root, dirs, files in os.walk("../all_stat/"):
    for filename in files:
        list_filename.append(filename)

list_final = []
for i in range(len(list_filename)):
	filenames = "../all_stat/" + list_filename[i]
	with open (filenames, 'rt') as in_file:
		for line in in_file:
			print(line)
