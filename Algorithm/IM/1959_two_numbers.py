import sys
sys.stdin = open('1959.txt')

T = int(input())
# for TC: 테스트케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_val = 0
    # 더 작은 리스트와 그 크기 설정
    if N > M:
        short_li, long_li = B, A
        N, M = M, N
    else:
        short_li, long_li = A, B
    # for 1: 킨 숫자열을 짧은 숫자열의 길이 만큼 순회하기 위한 시작점
    for i in range(0, M - N + 1):
        num_sum = 0
        # for 2: 짧은 숫자열의 크기만큼 반복
        for j in range(N):
            # 두 문자열의 곱을 누적합
            num_sum += long_li[i + j] * short_li[j]
        # 최댓값 갱신
        if max_val < num_sum:
            max_val = num_sum

    print(f'#{tc} {max_val}')