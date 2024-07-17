import requests

api_key = '65c9b65ea77ec6e5fe69df6ecc07d743'

CityName = input('Enter City Name: ')

URL ="https://api.openweathermap.org/data/2.5/weather?q="

CompleteURL= URL+CityName+"&appid="+api_key
response = requests.get(CompleteURL)


if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')

