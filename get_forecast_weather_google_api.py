# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: Mathieu Provost
"""

#imports
import time 
import datetime as dt

#own functions
from  myfunc import get_api_data, weather_data_call, format_forecast
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
base_url_forcast=data[2][:-1]
# city name
city_name=data[3][:-1]

#authentication to google api using JSON credential file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(base_path+'/api_data/WDcred2.json', scope)


def update_forecast(creds=creds,api_key=api_key,base_url=base_url_forcast,city=city_name):   
 
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
    wks_name= str((dt.datetime.now().timetuple().tm_yday +1 ) % 7)+' th'
    #wks_name= str((dt.datetime.now().hour) % 3 )+' th'
    
    #upload the forcast datafrane to the googlesheet
    d2g.upload(df_weather, spreadsheet_key, wks_name, credentials=creds, row_names=True)
    
    #sleep for one minute
    time.sleep(60)   
  
# Every day at 12am or 00:00 time bedtime() is called. 
#schedule.every().day.at("06:30").do(update_forecast) 
schedule.every().hour.do(update_forecast) 
  
# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(60)         
    