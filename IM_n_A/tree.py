import sys
sys.stdin = open('tree.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    height = list(map(int, input().split()))
    max_h = max(height)
    # 짝수 필요 수 0, 홀수 1
    num0 = 0
    num1 = 0
    for n in range(N):
        if max_h != height[n]:
            num0 += (max_h - height[n]) // 2
            num1 += (max_h - height[n]) % 2
    while abs(num0 - num1) >= 2:
        if num0 > num1:
            num0 -= 1
            num1 += 2
        elif num0 < num1:
            num0 += 1
            num1 -= 2
        else:
            break

    result = max(num0 * 2, (num1 * 2) - 1)
    # result = num0 * 2 + num1
    print(f'#{tc} {result}')