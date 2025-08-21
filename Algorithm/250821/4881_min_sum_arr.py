import itertools
import sys
sys.stdin = open('4881.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 인덱스 리스트
    i_lst = [i for i in range(N)]           # 0 ~ (N - 1)
    selected_index = itertools.permutations(i_lst, N)
    # 갱신할 최솟값을 담는 변수
    min_sum = 10 * N
    # 선택한 구성의 인덱스 순환
    for j in selected_index:
        # 합을 저장할 변수
        sum_set = 0

        # 행 순환
        for r in range(N):
            sum_set += arr[r][j[r]]
            # 현재까지의 최솟값이상이면 탈출
            if sum_set >= min_sum:
                break
        # 최솟값 갱신
        if min_sum > sum_set:
            min_sum = sum_set

    print(f'#{tc} {min_sum}')