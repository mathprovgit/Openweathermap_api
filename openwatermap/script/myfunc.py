# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:11:26 2020

@author: User
"""
def get_api_data():
    with open ("api_key/api_key.txt", "r") as myfile:
        data=myfile.readlines()
    #api_key = data[0]
    return data

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
def format_current(json_file):
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

def format_forcast(y):
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