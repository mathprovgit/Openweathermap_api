# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: User
"""

#imports
from time import sleep
#own functions
from  myfunc import get_api_data, weather_data_call,format_current
#google api
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authentication to openweathermap
data=get_api_data("api_data/info.txt")
# api key
api_key=data[0][:-1]
# base_urls
base_url_current=data[1][:-1]
#base_url_forcast=data[2][:-1]
# city name
city_name=data[3][:-1]

#authentication to google api using JSON credential file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('api_data/WDcred.json', scope)

#loop
while True:
    #get weather data from api        
    request=weather_data_call(api_key,base_url_current,city_name) 
    
    #format the data
    data_point_value=format_current(request)
    
    #append new data
    client = gspread.authorize(creds)
    
    #get current_weather_berlin sheet
    current_weather = client.open('current_weater_berlin')
    
    #append new data
    current_weather.sheet1.append_row(data_point_value)

    #wait 1 hours before next call
    sleep(60*15)
    
   