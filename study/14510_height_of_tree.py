import sys
sys.stdin = open('14510.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    # 짝수날 - 0, 홀수날 - 1
    cnt0 = 0
    cnt1 = 0
    # 나무 하나씩 검사
    for tree in trees:
        # 키가 홀수일 경우
        if tree % 2:
            # 홀수날 수 + 1,
            cnt1 += 1
            tree -= 1
            cnt0 += tree // 2
        # 키가 짝수일 경우
        else:
            cnt0 += tree // 2

    while abs(cnt0 - cnt1) > 2:
        if cnt0 > cnt1:
            cnt0 -= 1
            cnt1 += 2
        else:
            cnt0 += 1
            cnt1 -= 2

    result = max(cnt0 * 2, cnt1 * 2 + 1)

    print(f'#{tc} {result}')