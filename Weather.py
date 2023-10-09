import requests
import pprint
city = input('Enter your city: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8c1b2dd7998a81d7c2c627ff24a0bed&units=matric'.format(city)

res = requests.get(url)
data = res.json()

print(res)
print(data)