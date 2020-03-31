# Weather data 
-----

## Intro

### project goals
 - [x] get current and forecast weather data from api
 - [x] put data in a database json/csv format
 - [x] put the database online with google drive and google api
 - [ ] automatise the 3 previous step by loading the script on a rpi 0 that will do the job continuously
 - [ ] link the database to a public tableau and create a viz : [my public tableau](https://public.tableau.com/profile/mathieu.provost#!/)
 - [ ] create a maschine learning model to predict the weather 
 - [ ] compare the maschine learning prediction with the official forecast and determine the best
 
### Resourses 

#### Weather data provider:
- [openweathermap](https://openweathermap.org/)
- [DWD](https://www.dwd.de/)
- [CDC](https://cdc.dwd.de/portal/)

#### Code
for openweathermap
- https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
for dwdweather
- https://pypi.org/project/dwdweather2/
for google API
- https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2
python and googlesheets
- [sheet handling](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
- [pandas df to sheet](https://towardsdatascience.com/using-python-to-push-your-pandas-dataframe-to-google-sheets-de69422508f)

#### settings
for rpi settup:
 -[networ configuration for rpi0](https://kerneldriver.wordpress.com/2012/10/21/configuring-wpa2-using-wpa_supplicant-on-the-raspberry-pi/)
 - https://raspberrypihq.com/how-to-connect-your-raspberry-pi-to-wifi/
 -[system ctl 2](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
 -[copy usb to local](https://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/)
 -[numpy issu on pi](https://github.com/numpy/numpy/issues/14772)


## raspberry pi

The python script will be loaded to a raspberry pi 0. The job of the pi is to get the current and forecast weather data
 from openweather map api and update the googlesheet / Json database on google drive

 commands about the service
```python
sudo nano /lib/systemd/system/get_current_weather_ggapi.service # edit

sudo chmod 644 /lib/systemd/system/myscript.service # permission
#service handle
sudo systemctl daemon-reload 
sudo systemctl enable get_current_weather_ggapi.service
sudo systemctl start get_current_weather_ggapi.service
sudo systemctl status get_current_weather_ggapi.service
```

 -find files:
  ```find /path/to/folder/ -iname *file_name_portion*```

command to copy from usb
lsblk

``` cp -avr source desination```



 ## Tableau Public

 ## Mashine learning