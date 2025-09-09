import sys
import itertools
sys.stdin = open('2115.txt')

'''
N: 벌통의 크기
M: 선택할 수 있는 벌통의 개수
C: 꿀을 채취할 수 있는 최대 양
info: 각 벌통에서 채취할 수 있는 꿀의 양
'''


# 벌꿀꿀벌벌꿀벌꿀꿀벌 으앙아아아아아아

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    total_max_profit = 0

    max_profit_arr = [[0] * N for _ in range(N)]





    # print(f'#{tc} {result}')

