# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: User
"""

#imports
import time 

#own functions
from  myfunc import get_api_data, weather_data_call, format_current, format_forecast
#google api
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g

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
base_url_forcast=data[2][:-1]
# city name
city_name=data[3][:-1]

#authentication to google api using JSON credential file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(base_path+'/api_data/WDcred.json', scope)


def update_current(creds,api_key,base_url_current,city_name):
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

def update_forecast(creds,api_key,base_url_forcast,city_name):   
 
    #get weather data from api        
    request_f=weather_data_call(api_key,base_url_forcast,city_name) 
    
    try:
        #format the data
        df_weather=format_forecast(request_f)
       
    except:
        data_point_value=[]
        for i in range(12):
            data_point_value.append('open weather API error on forecast weather')

    #append new data
    client_f = gspread.authorize(creds)
        
    #get current_weather_berlin sheet
    forecast_weather = client_f.open('forecast_weather_berlin')
    
    # get workbook id
    spreadsheet_key = forecast_weather.id
    
    #replace the old forecast with the new
    wks_name='Sheet1'
    
    d2g.upload(df_weather, spreadsheet_key, wks_name, credentials=creds, row_names=True)


  
# After every hour geeks() is called. 
schedule.every().hour.do(update_current(creds,api_key,base_url_current,city_name)) 
  
# Every day at 12am or 00:00 time bedtime() is called. 
schedule.every().day.at("12:30").do(update_forecast(creds,api_key,base_url_current,city_name)) 
  
# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(60)         
    