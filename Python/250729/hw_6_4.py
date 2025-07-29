# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, val):
    # 새로운 딕셔너리에 인자로 받은 딕셔너리 복사
    new_dict = dictionary.copy()
    # 인자로 받은 key와 value를 딕셔너리에 추가
    new_dict.update({key: val})
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)