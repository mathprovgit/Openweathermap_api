# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:47 2020

@author: User
"""

# imports
from time import sleep
from  myfunc import get_api_data, weather_data_call,format_forcast

# get API data
data=get_api_data("api_data/info.txt")

# api key
api_key=data[0][:-1]
# base_urls
#base_url_current=data[1][:-1]
base_url_forcast=data[2][:-1]

# city name
city_name=data[3][:-1]
   
#loop
while True:
    #get data from api        
    request=weather_data_call(api_key,base_url_forcast,city_name)
    
    #create dataframe with formated data
    df_weather=format_forcast(request)
    
    #export 
    #export file name
    export_file_name='forecast/forcast_'+str(df_weather.index[0]).replace(' ','_').replace(':','-')
    
    #type
    export_type='csv'
    
    if export_type=='csv': #export to csv
        df_weather.to_csv(export_file_name+'.csv',sep=';')
    elif export_type=='json': #export to json
        with open(export_file_name+'.json', 'wb') as f:
            f.write(request.content)
    
    #wait 3 hours before next call
    sleep(3*3600)
