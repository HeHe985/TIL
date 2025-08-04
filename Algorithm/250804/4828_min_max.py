# 최솟값, 최댓값 구하기
# 버블 정렬 후 처음과 마지막 인덱스 출력

import sys

sys.stdin = open('input.txt')

# 총 테스트 케이스 수
T = int(input())
# 1부터 테스트 케이스 수까지 반복
for tc in range(1, T+1):
    # 배열의 크기
    N = int(input())
    arr =  list(map(int, input().split()))
    # 버블 정렬
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 최대/최소
    max_num = arr[len(arr)-1]
    min_num = arr[0]

    print(f'#{tc}', max_num - min_num)