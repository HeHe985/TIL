import sys
sys.stdin = open('4865.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    # str1의 문자를 키로 갖는 딕셔너리 생성
    dict_str = {i: 0 for i in str1}
    # str2의 문자와 딕셔너리의 키가 일치할때, 그 값에 +1
    for i in str2:
        if i in dict_str.keys():
            dict_str[i] += 1
    # 최댓값
    result = max(dict_str.values())

    print(f'#{tc} {result}')