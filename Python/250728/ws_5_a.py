N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.

# data_1 문자열의 N번째 요소를 arr_1 리스트에 추가
for i in range(N):
    arr_1.append(data_1[i])

print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

# data_2 문자열을 공백기준으로 분할해 arr_2 리스트에 할당
arr_2 = data_2.split()

# arr_2 리스트에서 홀수 요소만 출력
for i in arr_2:
    if int(i) % 2 == 1:
        print(i)
