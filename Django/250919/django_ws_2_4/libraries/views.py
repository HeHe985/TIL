import requests, os
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = os.getenv("API_KEY")


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)



def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '10',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'Year': '2023',
        'Month': '05',
        'Week': '3',

    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'title': item['title'],
            'author': item['author'],
            'pubDate': item['pubDate'],
            'isbn': item['isbn'],
            'salesPoint': item['salesPoint'],
            'bestDuration': item['bestDuration'],
        }
        result.append(info)
    result.sort(key=lambda x: x['salesPoint'], reverse=True)
    context = {
        'result': result
    }
    return render(request, 'bestseller.html', context)