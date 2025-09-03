import sys
sys.stdin = open('4837.txt')


# 조건을 만족하는 부분집합의 수를 계산하는 함수
def count_subset(a):
    # 조건을 만족하는 부분집합 수를 저장할 변수 cnt
    cnt = 0
    for i in range(1 << len(a)):
        # 부분집합의 길이를 계산할 변수
        len_subset = 0
        sum_of_subset = 0
        for j in range(len(a)):
            if i & (1 << j):
                # 해당 비트가 1일 경우 부분집합에 포함된 것이므로 len_subset +1
                len_subset += 1
                sum_of_subset += a[j]
        # 하나의 부분집합 계산을 완료했을 때
        # 부분집합의 길이가 N이고 합이 K이면 cnt +1
        if len_subset == N and sum_of_subset == K:
            cnt += 1
    return cnt


T = int(input())
A = [i for i in range(1, 13)]

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    result = count_subset(A)

    print(f'#{tc} {result}')