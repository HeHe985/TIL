import requests
from pprint import pprint
API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbgmlfla02191426001'
params = {
    'TTBKey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'SearchTarget': 'Book',
    'MaxResults': 50,
    'Output': 'js',
    'Version': 20131101,
}

response = requests.get(API_URL, params=params)
data = response.json()

items = data.get('item', [])
# 50개, 첵제목, 저자, 출간일 ISBN


books = []
for item in items:
    book = {
        '국제 표준 도서 번호': item.get('isbn'),
        '저자': item.get("author"),
        '제목': item.get("title"),
        '출간일': item.get("pubDate"),
    }
    books.append(book)

pprint(books)