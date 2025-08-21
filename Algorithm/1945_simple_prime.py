import sys
sys.stdin = open('1945.txt')


# 지수 계산 함수
def calculate_e(n, origin):
    cnt = 0
    while (origin % n) == 0:
        origin //= n
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = []
    for i in [2, 3, 5, 7, 11]:
        result.append(calculate_e(i, N))


    print(f'#{tc}', *result)