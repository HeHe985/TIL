# 아래 함수를 수정하시오.

# 짝수 요소 리스트 반환
def even_elements(list_element):
    '''
    인자로 받은 리스트를 순회하며 짝수 일때만 pop 메서드로 꺼내 새로운 리스트에 저장한다
    '''
    new_list = []
    new_list.extend([[i].pop() for i in list_element if i%2 == 0])
    return new_list
    
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = even_elements(my_list)
print(result)
