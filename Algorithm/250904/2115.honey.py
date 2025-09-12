import sys
import itertools
sys.stdin = open('2115.txt')

'''
N: 벌통의 크기
M: 선택할 수 있는 벌통의 개수
C: 꿀을 채취할 수 있는 최대 양
info: 각 벌통에서 채취할 수 있는 꿀의 양
'''

# 수익 계산 함수
def calculate(worker1, worker2):
    if



# 벌꿀꿀벌벌꿀벌꿀꿀벌 으앙아아아아아아

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    max_profit = 0
    positions = []
    for i in range(N):
        for j in range(M):
            positions.append((i, j))

    for worker1, worker2 in itertools.combinations(positions, 2):
        if worker1[0] == worker2[0] and abs(worker1[1] - worker2[1]) < M:
            continue


    # max_profit_arr = [[0] * N for _ in range(N)]


    # print(f'#{tc} {result}')

