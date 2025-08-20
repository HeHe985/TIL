from collections import deque
import sys
sys.stdin = open('5099.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = deque(map(int, input().split()))
    chk = [True] * N
    oven = []
    for i in range(M):
        oven.append(C.popleft())
    while chk:
        for j in range(N):
            if oven[j] != 0:
                continue
            # 치즈가 0이고, 구울 피자가 남아 있을때
            elif C:
                oven[j] = C.popleft()
            # 치즈 0, 남은 피자 없을 때
            else:
                chk[j] = False



    print(f'#{tc} {result}')



            #
            #
            # cheese = oven.popleft()
            # cheese //= 2
            # if cheese > 0:
            #     oven.append(cheese)
            #
            # elif C:
            #     oven.appendleft(C.fdfsdfds)
            # else:
            #     result = j + 1
            #





'''
from collections import deque
import sys
sys.stdin = open('5099.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = [[idx, val] for idx, val in enumerate(map(int, input().split()), 1)]

    pizza_oven = []

    for i in range(N):
        pizza_oven.append(C.pop(0))

    while len(pizza_oven) > 1:
        pizza_num, cheese = pizza_oven.pop(0)
        cheese //= 2

        if cheese != 0:
            pizza_oven.append([pizza_num, cheese])
        elif C:
            pizza_oven.append(C.pop(0))

    print(f'#{tc} {pizza_oven[0][0]}')
'''