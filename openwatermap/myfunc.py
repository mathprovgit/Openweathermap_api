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
    vals=[str(dt.datetime.fromtimestamp(y['dt'])), # 
          round((y['main']['temp']-273.15),2),
          round((y['main']['humidity']),2),
          round((y['main']['pressure']),2),
          round((y['wind']['speed']),2),
          y['wind']['deg'],
          y['clouds']['all'],
          y['weather'][0]['main'],
          y['weather'][0]['description'],
          y['weather'][0]['icon'],
          str(dt.datetime.fromtimestamp(y['sys']['sunrise'])).split(' ')[1],
          str(dt.datetime.fromtimestamp(y['sys']['sunset'])).split(' ')[1]         
         ]
    return vals

def format_forcast(request):
    y=request.json()
    weather_data=[]
    for i in range(len(y['list'])):
        weather_data.append([y['list'][i]['dt_txt'],
                             y['list'][i]['main']['temp'],
                             y['list'][i]['main']['humidity'],
                             y['list'][i]['wind']['speed'],
                             y['list'][i]['wind']['deg'],
                             y['list'][i]['weather'][0]['main']
                            ])

    df_weather=pd.DataFrame(weather_data,columns=['datetime','temp','humidity','wind_speed','wind_dir','weather'])
    df_weather.set_index(pd.to_datetime(df_weather.datetime),inplace=True)
    df_weather.drop('datetime',axis=1,inplace=True)
    #kelvin to degree
    df_weather['temp']=df_weather['temp']-273.15
    return df_weather