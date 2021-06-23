import requests
from datetime import datetime

api_key="4955442bb818e814af2e7a75e3f1ab42"

location=input("enter the city name : ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

try:
    #now creating a get request:-
    api_link=requests.get(complete_api_link)

    #now taking the data in json format:-
    api_data=api_link.json()# json format is just like the dictionary in python.

    # adding try and except to display the desired output if the user enters wrong city name:- 

    temp_city=((api_data['main']['temp']) - 273.15)#conversion of temp from kelvin to celcius.
    '''
            api_data is the dictionary which contains whole data.

            "main": {
                "temp": 282.55,#we want temperature from main dictionary.
                "feels_like": 281.86,
                "temp_min": 280.37,
                "temp_max": 284.26,
                "pressure": 1023,
                "humidity": 100
              }
    '''
    weather_desc=api_data["weather"][0]["description"]
    '''
             "weather": [
                {
                  "id": 800,
                  "main": "Clear",
                  "description": "clear sky",#we want weather discription from weather key which contains a list as its value and the it contains a description key.
                  "icon": "01d"
                }
              ]
    '''
    humidity=api_data["main"]["humidity"]
    '''
            "main": {
                "temp": 282.55,
                "feels_like": 281.86,
                "temp_min": 280.37,
                "temp_max": 284.26,
                "pressure": 1023,
                "humidity": 100
              }
    '''
    wind_speed=api_data["wind"]["speed"]
    '''
            "wind": {
                "speed": 1.5,
                "deg": 350
              }
    '''
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-".center(50,"-"))
    print("Weather Stats for {} || {}".format(location.upper(),date_time))
    print("-".center(50,"-"))

    print("Current Temperature is : {:.2f} degree C".format(temp_city))
    print("Current Weather Discription : {}".format(weather_desc))
    print("Current Humidity : {}".format(humidity))
    print("Current Wind Speed : {}".format(wind_speed))

    #Storing the data in text file :-
    with open("weather_data.txt","a") as wd:
        wd.write("Weather Stats for ")
        wd.write(location.upper())
        wd.write("  ||  ")
        wd.write(date_time)
        wd.write("\n")
        wd.write(str(temp_city))
        wd.write("\n")
        wd.write(weather_desc)
        wd.write("\n")
        wd.write(str(humidity))
        wd.write("\n")
        wd.write(str(wind_speed))
        wd.write("\n")
        wd.close()

    #Fetching saved in text file:-
    print("\n\n","_".center(50,"_"))
    print("PREVIOUS DATA STORED IN FILE :-")
    print("_".center(50,"_"))
    
    l=["Current Temperature : ","Weather Description : ","Humidity : ","Wind Speed : "]
    with open("weather_data.txt","r") as rw:
        str="\n"
        print(str)
        while str:
            str=rw.readline()
            if(str!=""):
                print(str)
                for i in range(0,4):
                    print(l[i],end="")
                    str=rw.readline()
                    print(str)
                print(".".center(65,"."))
        rw.close()
except:
  print("**ERROR OCCURED** \nthese are some reasons for the error :-\n => May be you entered invalid city name\n => you are not connected to the internet")


#OUTPUT:-(I have shown here output because in my compiler it is executing properly and in online compiler(replit.com) also it is executing properly , it may be possible that it does not execute properly in ohter compiler(may be in colab also))
'''
enter the city name : kota
--------------------------------------------------
Weather Stats for KOTA || 22 Jun 2021 | 09:50:17 PM
--------------------------------------------------
Current Temperature is : 33.27 degree C
Current Weather Discription : broken clouds
Current Humidity : 45
Current Wind Speed : 7.77


 __________________________________________________
PREVIOUS DATA STORED IN FILE :-
__________________________________________________


Weather Stats for JAIPUR  ||  22 Jun 2021 | 09:28:34 PM

Current Temperature : 34.620000000000005

Weather Description : haze

Humidity : 38

Wind Speed : 2.57

.................................................................
Weather Stats for JAIPUR  ||  22 Jun 2021 | 09:30:11 PM

Current Temperature : 34.620000000000005

Weather Description : haze

Humidity : 38

Wind Speed : 2.57

.................................................................
Weather Stats for RANCHI  ||  22 Jun 2021 | 09:34:56 PM

Current Temperature : 23.060000000000002

Weather Description : haze

Humidity : 100

Wind Speed : 3.09

.................................................................
Weather Stats for RANCHI  ||  22 Jun 2021 | 09:37:06 PM

Current Temperature : 23.060000000000002

Weather Description : haze

Humidity : 100

Wind Speed : 3.09

.................................................................
Weather Stats for JAIPUR  ||  22 Jun 2021 | 09:38:02 PM

Current Temperature : 34.620000000000005

Weather Description : haze

Humidity : 38

Wind Speed : 2.57

.................................................................
Weather Stats for JAIPUR  ||  22 Jun 2021 | 09:39:45 PM

Current Temperature : 34.620000000000005

Weather Description : haze

Humidity : 38

Wind Speed : 2.57

.................................................................
Weather Stats for UDAIPUR  ||  22 Jun 2021 | 09:40:50 PM

Current Temperature : 25.220000000000027

Weather Description : overcast clouds

Humidity : 75

Wind Speed : 2.67

.................................................................
Weather Stats for KOTA  ||  22 Jun 2021 | 09:43:49 PM

Current Temperature : 33.27000000000004

Weather Description : broken clouds

Humidity : 45

Wind Speed : 7.77

.................................................................
Weather Stats for JAIPUR  ||  22 Jun 2021 | 09:45:29 PM

Current Temperature : 34.620000000000005

Weather Description : haze

Humidity : 38

Wind Speed : 2.57

.................................................................
Weather Stats for KOTA  ||  22 Jun 2021 | 09:50:17 PM

Current Temperature : 33.27000000000004

Weather Description : broken clouds

Humidity : 45

Wind Speed : 7.77

.................................................................
'''
