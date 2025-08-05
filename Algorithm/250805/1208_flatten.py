'''
상자 높이 리스트를 오름차순 정렬
최대 덤프횟수 안에서 반복을 돌리고
맨 뒤 요소에서 맨 앞 요소로 dump
다시 오름차순 정렬~~~계속 반복
반복이 끝나기전 평탄화가 완료되면 break
최고점과 최저점 높이 차를 반환
'''

import sys
sys.stdin = open('1208.txt')
T = 10

for tc in range(1, T + 1):
    n_dump = int(input())
    arr = sorted(list(map(int, input().split())))
    for j in range(n_dump):
        arr[-1], arr[0] = arr[-1] - 1, arr[0] + 1
        arr.sort()
        # 평탄화 여부 확인
        if arr[-1] - arr[0] <= 1:
            break
    result = arr[-1] - arr[0]
    print(f'#{tc} {result}')