# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))    # 없는 키는 None 반환
print(person.get('country', '해당 키는 존재하지 않습니다'))
print(person['name'])   #대괄호 접근법에서는 없는 키에 접근했을 때 키에러가 발생해 그 아래 코드부터 중단됨
# print(person['country'])  # KeyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age'])
for key in person.keys():   # 순회가능하다 >>> 활용가능
    print(key)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for value in person.values():   # 순회가능
    print(value)

# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)]) >>> 튜플
for key, value in person.items():   # 이터러블에서 튀어나오는게 쌍으로된 튜플이기 때문에 임시변수 두개 필요
    print(key, value)

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'

# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)

# setdefault    키가 없다면 default롸 연결한 키를 딕셔너리에 추가하고 default를 반환
person = {'name': 'Alice', 'age': 25}   # .get()은 조회했을때 없으면 땡
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person.setdefault('name', 'KOREA'))   # Alice 있는 키를 조회하면 변경 안되고 원래 값 그대로 나옴
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(person)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}


'''
아래의 두 경우는 전혀 다르다. 리스트에서도 적용되는 내욜
'''
# 똑같은 딕셔너리 유지
D1 = {'name': 'Alice', 'age': 25}
D1.clear()

# 재할당(다른 딕셔너리가 된 것)
D2 = {'name': 'Alice', 'age': 25}
D2 = {}