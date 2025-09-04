import sys
sys.stdin = open('5188.txt')

# 우, 하 델타
dx = [0, 1]
dy = [1, 0]
T = int(input())


def sum_min(x, y, total):
    global result
    # 기저 조건: 끝 칸에 도달시 종료
    if x == N - 1 and y == N - 1:
        result = min(total, result)
        return
    # 가지치기: 지금까지의 합계가 이미 현재까지의 최솟값이상일시 탐색 종료
    elif total >= result:
        return
    # 델타 탐색
    for d in range(2):
        nx, ny = x + dx[d], y + dy[d]
        # 범위 안이면 다음 좌표로 재귀 호출
        if 0 <= nx < N and 0 <= ny < N:
            sum_min(nx, ny, total + arr[nx][ny])


# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N * N
    sum_min(0, 0, arr[0][0])

    print(f'#{tc} {result}')



'''
# 비트 마스크를 이용하여 부분집합 개념을 적용하였으나 시간 초과
import sys
sys.stdin = open('5188.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탐색 시작
    min_sum = 10 * N * N
    # 시작 칸에서 우 또는 하를 선택해야는 갈림길의 수
    choice_n = (N - 1) * 2
    # 비트마스크로 부분집합 순회
    for i in range(1 << choice_n):
        # 우, 하가 각각 N-1이어야 함
        right = bin(i).count('1')
        down = choice_n - right
        if down != N - 1 or right != N - 1:
            continue
        # 초기 좌표, 부분집합의 합 값 지정
        x, y = 0, 0
        sum_of_subset = arr[0][0]
        # 각 부분 집합의 비트를 순회하며
        for j in range(choice_n):

            # 1이면 우를 선택
            if i & (1 << j):
                nx, ny = x, y + 1
            # 0이면 하를 선택
            else:
                nx, ny = x + 1, y
            # 이동한 칸의 값을 더해주고 위치 업데이트
            sum_of_subset += arr[nx][ny]
            x, y = nx, ny
            # 현재까지의 부분집합의 합이 이미 최소를 넘었다면 break
            if sum_of_subset >= min_sum:
                break
        # 최솟값 계산산
        min_sum = min(min_sum, sum_of_subset)

    print(f'#{tc} {min_sum}')
'''