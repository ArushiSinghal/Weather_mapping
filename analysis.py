#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

data = pd.read_csv("a5.csv", sep=",")
df = data.values
df = np.insert(df, np.size(df,1), 0, axis=1)
for i in range(np.size(df,0)):
    df[i][4] = df[i][1] + df[i][2]
print (df)
