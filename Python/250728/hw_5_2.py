# 아래 함수를 수정하시오.

# 특정 문자 개수 세기
def count_character(string_element, character):
    '''
    count 메서드 사용하여 문자열에서 특정 문자 개수 반환
    '''
    return string_element.count(character)


result = count_character("Hello, World!", "o")
print(result)  # 2
