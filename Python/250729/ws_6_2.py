# 아래 함수를 수정하시오.
# 딕셔너리와 키를 인자로 받아 해당 값을 반환, 존재하지 않을 경우 'Unknown' 반환
def get_value_from_dict(dict, key):
    return dict.get(key, 'Unknown')

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown
