# 아래 함수를 수정하시오.

# 첫글자를 대문자로 변경
def capitalize_words(original_string):
    '''
    title 메서드를 이용해 각 단어의 첫글자를 대문자로 변환하여 반환 
    '''
    return original_string.title()

result = capitalize_words("hello, world!")
print(result)
