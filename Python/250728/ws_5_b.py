data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

# data_1 문자열 중 대문자이거나 공백인 요소만 줄바꿈 없이 출력
for i in data_1:
    if i.isupper() is True or i == ' ':
        print(i, end='')

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

# 각 글자들의 위치한 index 번호를 찾아 arr 리스트에 추가
for i in '내힘들다':
    arr.append(data_2.find(i))
print(arr)

# arr 리스트 오름차순 정렬
arr.sort()
print(arr)

# data_2에서 arr 리스트의 각 요소번째의 문자열 줄바꿈 없이 출력
for i in arr:
    print(data_2[i], end='')