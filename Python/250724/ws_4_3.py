import requests
from pprint import pprint as print

i = 0
dummy_data  = []

for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    if (-80 < float(parsed_data['address']['geo']['lat']) < 80) and (-80 < float(parsed_data['address']['geo']['lng']) < 80):
        dummy_data.append({'name': parsed_data['name'], 'lat': parsed_data['address']['geo']['lat'], 'lng': parsed_data['address']['geo']['lng'], 'company': parsed_data['company']['name']})

print(dummy_data)
