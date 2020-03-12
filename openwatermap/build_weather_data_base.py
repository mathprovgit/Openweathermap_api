# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import pandas as pd
import numpy as np
import datetime as dt
import requests, json 

with open ("api_key/api_key.txt", "r") as myfile:
    data=myfile.readlines()
api_key = data[0]

# base_url variable to store url 
base_url =  "http://api.openweathermap.org/data/2.5/forecast?"
# Give city name 
city_name = 'Berlin,de'
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

response = requests.get(complete_url) 
  
# json method of response object  
x = response.json() 