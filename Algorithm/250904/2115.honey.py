import sys
import itertools
sys.stdin = open('2115.txt')

'''
N: 벌통의 크기
M: 선택할 수 있는 벌통의 개수
C: 꿀을 채취할 수 있는 최대 양
arr: 각 벌통에서 채취할 수 있는 꿀의 양
'''

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # M칸 짜리 정보를 가지는 배열
    # M_arr = [[i, j] for j in range(N - M) for i in range(N)]
    M_arr = [[] * (N- M) for _ in range(N)]
    for i in range(N):
        for j in range(N - M):
            M_arr[i][j] = [i, j]

    subsets = list(itertools.combinations(M_arr, 2))
    max_honey = 0
    for subset in subsets:
        sum_honey = 0
        if subset[0][0] == subset[1][0]:
            if subset[0][1] <= subset[1][1] <= subset[0][1] + M - 1:
                continue
            for k in range(M):
                for l in range(2):
                    if arr[subset[l][0]][subset[l][1] + k] > C:
                        sum_honey += C**2
                    else:
                        sum_honey += (arr[subset[l][0]][subset[l][1] + k])**2
        max_honey = max(max_honey, sum_honey)

    print(f'#{tc} {max_honey}')