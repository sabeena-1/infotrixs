import requests

from pprint import pprint

city = input('Enter your city: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8c1b2dd7998a81d7c2c627ff24a0bed&units=matric'.format(city)
res = requests.get(url)

data = res.json()
print(res)
print(data)
pprint(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

print('Temperature: {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude:{}'.format(latitude))
print('Longitude:{}'.format(longitude))
print('Description:{}'.format(description))
