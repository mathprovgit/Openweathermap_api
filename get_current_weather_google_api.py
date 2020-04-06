# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: Mathieu Provost
"""

#imports
import time 


#own functions
from  myfunc import get_api_data, weather_data_call, format_current
#google api
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#os
import os

#scheduler
import schedule


# Authentication to openweathermap
base_path=os.getcwd()
#base_path="/home/mathieu/python_project/weather"

data=get_api_data(base_path+"/api_data/info.txt")
# api key
api_key=data[0][:-1]
# base_urls
base_url_current=data[1][:-1]
#base_url_forcast=data[2][:-1]
# city name
city_name=data[3][:-1]

#authentication to google api using JSON credential file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(base_path+'/api_data/WDcred.json', scope)


def update_current(creds=creds,api_key=api_key,base_url=base_url_current,city=city_name):
    #get weather data from api        
    request=weather_data_call(api_key,base_url_current,city_name) 
    
    try:
        #format the data
        data_point_value=format_current(request)
       
    except:
        data_point_value=[]
        for i in range(12):
            data_point_value.append('open weather API error on current weather')

    #append new data
    client = gspread.authorize(creds)
        
    #get current_weather_berlin sheet
    current_weather = client.open('current_weather_berlin')
    
    #append new data
    current_weather.sheet1.append_row(data_point_value)

  
# After every hour geeks() is called. 
schedule.every().hour.do(update_current) 
   
# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(60)         
    