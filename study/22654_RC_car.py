import sys
sys.stdin = open('22654.txt')

# 상 우 하 좌
direction = set(0, 1, 2, 3)
T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    field = [input() for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        C, command = map(input().split())
        commands = (int(C), command)




    # print(f'#{tc} {result}')