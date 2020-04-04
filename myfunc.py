# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:11:26 2020

@author: User
"""

import requests
#import json
import datetime as dt 
import pandas as pd

def get_api_data(path__file):
    with open (path__file, "r") as myfile:
        data=myfile.readlines()
    return data

def weather_data_call(api_key,base_url,city_name):    
    # base_url variable to store url 
    base_url =  base_url

    # Give city name 
    city_name = city_name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    return response

# format values from the response
def format_current(request):
    y=request.json()
    errormessage="not available"
    
    try:
        datetime=str(dt.datetime.fromtimestamp(y['dt']))
    except:
        datetime=errormessage
        
    try:
        temp=round((y['main']['temp']-273.15),2)
    except:
        temp=errormessage
        
    try:
        humidity=round((y['main']['humidity']),2)
    except:
        humidity=errormessage
        
    try:
        pressure=round((y['main']['pressure']),2)
    except:
        pressure=errormessage
        
    try:
        windspeed=round((y['wind']['speed']),2)
    except:
        windspeed=errormessage
        
    try:
        winddir=y['wind']['deg']
    except:
        winddir=errormessage
    
    try:
        cloudcov=y['clouds']['all']
    except:
        cloudcov=errormessage
    
    try:
        rain=y['rain']['1h']
    except:
        rain=0
        
    try:
        snow=y['snow']['1h']
    except:
        snow=0
        
    try:
        weather=y['weather'][0]['main']
    except:
        weather=errormessage
        
    try:
        description=y['weather'][0]['description']
    except:
        description=errormessage
    
    try:
        icon=y['weather'][0]['icon']
    except:
        icon=errormessage
        
    try:
        sunrise=str(dt.datetime.fromtimestamp(y['sys']['sunrise'])).split(' ')[1]
    except:
        sunrise=errormessage
        
    try:
        sunset=str(dt.datetime.fromtimestamp(y['sys']['sunset'])).split(' ')[1]
    except:
        sunset=errormessage

    return [datetime, temp, humidity, pressure, windspeed, winddir, cloudcov,
            weather,rain,snow, description,icon, sunrise, sunset]

def format_forecast(request):
    errormessage="not available"
    y=request.json()  
    weather_data=[]
    for i in range(len(y['list'])):
        try:
            datetime=y['list'][i]['dt_txt']
        except:
            datetime=errormessage
            
        try:
            temp=round(y['list'][i]['main']['temp'],2)
        except:
            temp=errormessage
            
        try:
            humidity=(y['main']['humidity'])
        except:
            humidity=errormessage
            
        try:
            pressure=y['list'][i]['main']['pressure']
        except:
            pressure=errormessage
            
        try:
            windspeed=round(y['list'][i]['wind']['speed'],1)
        except:
            windspeed=errormessage
            
        try:
            winddir=y['list'][i]['wind']['deg']
        except:
            winddir=errormessage
        
        try:
            cloudcov=y['list'][i]['clouds']['all']
        except:
            cloudcov=errormessage
            
        try:
            rain=y['list'][i]['rain']['3h']
        except:
            rain=0
        
        try:
            snow=y['list'][i]['snow']['3h']
        except:
            snow=0
            
        try:
            weather=y['list'][i]['weather'][0]['main']
        except:
            weather=errormessage
            
        try:
            description=y['list'][i]['weather'][0]['description']
        except:
            description=errormessage
        
        try:
            icon=y['list'][i]['weather'][0]['icon']
        except:
            icon=errormessage
            
        weather_data.append([datetime, temp, humidity, pressure, windspeed, winddir, cloudcov,
            rain, snow, weather, description,icon])

    df_weather=pd.DataFrame(weather_data,columns=['datetime','temp','humidity','pressure','wind_speed','wind_dir','cloudcoverage','rain3h','snow3h','weather','description','icon'])
    df_weather.set_index(pd.to_datetime(df_weather.datetime),inplace=True)
    df_weather.drop('datetime',axis=1,inplace=True)
    #kelvin to degree
    df_weather['temp']=round(df_weather['temp']-273.15,2)
    return df_weather