import sys
sys.stdin = open('20551.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    cnt = 0
    result = 0
    # C보다 B가 더 크면
    if B >= C:
        # B를 C보다 1 더 작게 만들고
        cnt += B - C + 1
        B = C - 1
        # 0이면 결과는 -1
        if B == 0:
            cnt = -1
    # 이전 결과가 -1이 아니고 A가 B보다 더 크면
    if cnt >= 0 and A >= B:
        # A를 B보다 1 더 작게 만들고
        cnt += A - B + 1
        A = B - 1
        # 0이라면 결과는 -1
        if A == 0:
            cnt = -1

    print(f'#{tc} {cnt}')