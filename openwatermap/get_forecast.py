# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:07:13 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: User
"""

# imports
import os
import datetime as dt
import requests, json 
import csv
from time import sleep

#get api key
with open ("api_key/api_key.txt", "r") as myfile:
    data=myfile.readlines()
api_key = data[0]
base_url = 
city_name =

#get data
def weather_data_call(api_key):
    
    # base_url variable to store url 
    base_url =  "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = 'Berlin,de'
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    return response

# format values from the response
def format_values(json_file):
    vals=[str(dt.datetime.fromtimestamp(json_file['dt'])), # 
          round((json_file['main']['temp']-273.15),2),
          round((json_file['main']['humidity']),2),
          round((json_file['main']['pressure']),2),
          round((json_file['wind']['speed']),2),
          json_file['wind']['deg'],
          json_file['clouds']['all'],
          json_file['weather'][0]['main'],
          json_file['weather'][0]['description'],
          json_file['weather'][0]['icon'],
          str(dt.datetime.fromtimestamp(json_file['sys']['sunrise'])).split(' ')[1],
          str(dt.datetime.fromtimestamp(json_file['sys']['sunset'])).split(' ')[1]         
         ]
    
    return vals

#build for tests
#x=weather_data_call(api_key) un comment for the real

#build test weather data   
#with open('weather_test.json', 'wb') as f:
#    f.write(x.content)

#get test weather data
with open('weather_test.json') as f:
    data = json.load(f)
#x=data    
    
#loop
#for test
i=0 
while True:
    
    #get data from api        
    x=weather_data_call(api_key) #un comment for the real
    #x=data
    
    #export file name
    export_file_name='current/current_weater_berlin.csv'

    #data header
    header=["datetime","temperature","humidity","pressure","windspeed","winddir","cloudcoverage","weather","description","weathericon","sunrisetime","sunsettime"]

    #create data point
    data_point=dict(zip(header, format_values(x.json())))
    #data_point=dict(zip(header, format_values(x)))
    #append to file
    with open(export_file_name, 'a', newline='') as f:
        writer = csv.DictWriter(f,delimiter=',',fieldnames=header)
        if os.path.getsize(export_file_name)==0:
               writer.writeheader()          
        writer.writerow(data_point)

    #if i>=3:
    #    break
    #i+=1
    
    sleep(1200)
#x.content
#x.json()