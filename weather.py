import requests
from datetime import datetime
user_api="ad192de52a3a24431ab1c95f5917bf22"
# location=input("Enter the City Name: ")


def Weather(city_name):
    complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=ad192de52a3a24431ab1c95f5917bf22"
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()

    if api_data['cod']=='404':
        print("Invalid City :{},Please check your city name".format(city_name))
    else:
        temp_city=((api_data['main']['temp'])-273.15)
        weather_desc=api_data['weather'][0]['description']
        hmdt=api_data['main']['humidity']
        wind_spd=api_data['wind']['speed']
        # date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        # print("----------------------------------------------------------")
        # print("Weather Stats for - {} || {}".format(city_name.upper(),date_time))
        # print("----------------------------------------------------------")
        #
        # print("Current Temparature is : {:.2f} deg C".format(temp_city))
        # print("Current weather desc : ",weather_desc)
        # print("Current Humidity : ",hmdt,'%')
        # print("Current wind speed : ",wind_spd,'kmph')

        return temp_city, weather_desc, hmdt, wind_spd

# Weather("Delhi")