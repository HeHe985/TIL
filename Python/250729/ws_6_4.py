# 아래 함수를 수정하시오.

# 넘겨받은 딕셔너리의 모든 키를 리스트로 반환
def get_keys_from_dict(dict):
    return list(dict.keys())

def get_all_keys_from_dict(dictionary):
    # 빈 리스트 생성
    key_list = []
    # 넘겨받은 딕셔너리의 키와 값으로 순회
    for key, value in dictionary.items():
        # 현재 키를 key_list에 추가
        key_list.append(key)
        # 현재 키에 해당하는 값이 딕셔너리 형이면,
        # 값에 해당하는 딕셔너리를 넘겨주며 다시 자기자신 함수 호출
        if isinstance(value, dict):
            key_list.extend(get_all_keys_from_dict(value))
    return key_list

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
