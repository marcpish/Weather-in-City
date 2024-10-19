import requests

//api_key
user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    country = weather_data.json()['sys']['country']
    print(f"The temperature in {user_input} is {temp} degrees F")
    print(f"The country {user_input} is in: {country}")

      

