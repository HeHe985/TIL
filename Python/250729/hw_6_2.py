# 아래 함수를 수정하시오.
# 넘겨 받은 리스트를 set으로 형변환
def remove_duplicates_to_set(lst):
    return set(lst)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
