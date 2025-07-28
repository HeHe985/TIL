
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# original_word 문자열을 모두 나눠 arr 리스트에 추가
arr.extend(list(original_word))
print(arr)

# 문장에서 잘못된 내용을 제거하는 함수
def restructure_word(word, arr):
    '''
    word 문자열을 순회하며 숫자일 경우 해당 숫자만큼 반복하여 arr 리스트의 마지막 요소 제거
    그 외의 경우 arr 리스트에서 해당 요소 제거
    '''
    for i in word:
        if i.isdecimal():
            for j in range(int(i)):
                arr.pop()
        else:
            arr.remove(i)
    return arr

# 함수 호출 결과 result에 할당
result = restructure_word(word, arr)
print(result)

# result에 할당된 리스트를 하나의 문자열로 변환하여 출력
print(''.join(result))
