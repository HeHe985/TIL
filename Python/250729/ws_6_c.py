data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

# data를 순회
for element in data:
    # key_list 순회
    for key in key_list:
         # key_list로 얻은 key가 없다면, key에 'unknown' 할당
         element.setdefault(key, 'unknown')
         print(f'{key} 은/는 {element.get(key)}입니다.')
    print()