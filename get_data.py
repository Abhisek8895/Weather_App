import requests
import pytz
from timezonefinder import TimezoneFinder
import datetime
import os
from dotenv import load_dotenv

def get_info(city):

    load_dotenv()

    url = os.getenv("URL")
    api = os.getenv("API_KEY")
    # city = "Toronto"

    # print(url)
    # print(api)


    data = requests.get(url+city+api).json()
    # print(data)

    desc = data['weather'][0]['main']

    temp_cel = round(data["main"]["temp"] - 273.15)
    # temp_cel = "{0:.2f}".format(temp_cel)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    cloud = data['clouds']['all']
    icon = data['weather'][0]['icon']


    lon = data["coord"]["lon"]
    lat = data["coord"]["lat"]

    # To get the Time , Date and Day
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=lon, lat=lat)
    home = pytz.timezone(result)
    local_time= datetime.datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    current_date = local_time.strftime("%d/%m/%Y")
    now = datetime.datetime.now()
    day = now.strftime("%A")
    print(now.strftime("%A"))
    return temp_cel, desc, current_date, current_time, day, pressure, humidity, wind, cloud, icon
    # print("{0:.2f}".format(temp_cel))
    # print(current_time)
    # print(current_date)