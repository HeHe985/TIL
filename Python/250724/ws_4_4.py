import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

dummy_data  = []

for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    if (-80 < float(parsed_data['address']['geo']['lat']) < 80) and (-80 < float(parsed_data['address']['geo']['lng']) < 80):
        dummy_data.append({'name': parsed_data['name'], 'lat': parsed_data['address']['geo']['lat'], 'lng': parsed_data['address']['geo']['lng'], 'company': parsed_data['company']['name']})

#print(dummy_data)

def create_user(user_list):
    censored_user_list = {}
    for i in user_list:
        if censorship(i) is True:
            censored_user_list[i['company']] = [i['name']]
    return censored_user_list


def censorship(j):
    if j['company'] in black_list:
        print(f'{j["company"]} 소속의 {j["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user(dummy_data))