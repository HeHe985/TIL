def restructure_word(word, arr):
    # 인자로 받은 word 문자열을 순회
    for char in word:
        # 만약 char가 숫자 문자열이라면,
        if char in '0123456789':
        # if a in [1, 2, 3, 4, 5]:  같은 표현
        # if char.isdecimal() is True:
            # 그 숫자만큼 반복
            for i in range(int(char)):
                arr.pop()
        # 문자가 숫자 문자열이 아니라면,
        else:
            #remove로 해당 문자열 제거
            arr.remove(char)
    return arr


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
# 원본 문자열의 각 문자를 리스트의 요소로 분해하여 arr에 저장
arr.extend(original_word)
# arr를 출력
print(arr)

result = restructure_word(word, arr)
