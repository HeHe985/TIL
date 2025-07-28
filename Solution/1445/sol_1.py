def count_character(text, char):
    '''
    주어진 문자열(text)에서 특정 문자(char)의 개수를 반환하는 함수
    '''
    # 몇번 등장했는지 누적되는 수
    result = 0
    # 주어진 문자열을 순회하면서
    for ch in text:
        # text의 요소인 ch와 주어진 특정 문자 char를 비교
        # ch와 chat가 같다면
        if ch == char:
            # 몇번 등장한건지 카운팅
            result += 1
            # print(result)
    return result




result = count_character("Hello, World!", "o")
print(result)  # 2
