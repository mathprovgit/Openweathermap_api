# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: User
"""

# imports
import os
import csv
from time import sleep
#own functions
from  myfunc import get_api_data, weather_data_call,format_current

# get API data
data=get_api_data("api_data/info.txt")

# api key
api_key=data[0][:-1]
# base_urls
base_url_current=data[1][:-1]
#base_url_forcast=data[2][:-1]

# city name
city_name=data[3][:-1]

if False:
    import json
    #build for tests
    #x=weather_data_call(api_key,base_url_current,city_name)
    
    #build test weather data   
    #with open('weather_test.json', 'wb') as f:
    #    f.write(x.content)
    
    #get test weather data
    with open('weather_test.json') as f:
        data = json.load(f)
  
    
#loop
#i=0
while True:
    #get data from api        
    request=weather_data_call(api_key,base_url_current,city_name)   
    #request=data
    
    #export file name
    export_file_name='current/current_weater_berlin.csv'

    #data header
    header=["datetime","temperature","humidity","pressure","windspeed","winddir","cloudcoverage","weather","description","weathericon","sunrisetime","sunsettime"]

    #create data point
    data_point=dict(zip(header, format_current(request)))
    #data_point=dict(zip(header, format_values(x)))
    #append to file
    with open(export_file_name, 'a', newline='') as f:
        writer = csv.DictWriter(f,delimiter=',',fieldnames=header)
        if os.path.getsize(export_file_name)==0:
               writer.writeheader()          
        writer.writerow(data_point)


    #wait 1 hours before next call
    sleep(3600)
    
    #sleep(1)
    #if i>=3:
    #    break
    #i+=1