import sys
import itertools
sys.stdin = open('5189.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 100 * N
    # 부분집합 인덱스 생성(시작은 무조건 0: 사무실)
    idx_list = [i for i in range(1, N)]
    perms = list(itertools.permutations(idx_list))

    # 각 순열을 순회
    for perm in perms:
        # 마지막은 무조건 0: 사무실
        path = [*perm] + [0]

        # 소비량의 합계의 초기값을 0 -> 순열의 첫요소로 지정
        sum_consumption = arr[0][path[0]]
        # 마지막 요소 직전까지 순회하며 소비량 합계 계산
        for i in range(N - 1):
            sum_consumption += arr[path[i]][path[i + 1]]

        # min 갱신
        min_sum = min(min_sum, sum_consumption)

    print(f'#{tc} {min_sum}')