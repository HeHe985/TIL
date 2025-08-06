import sys

sys.stdin = open('input.txt')


T = int(input())

# 상, 하, 좌, 우 델타 정의
# dr은 행의 변화량(상/하)
# dc는 열의 변화량(좌/우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    # N 값 설정
    N = int(input())

    # 이차원 배열 설정
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    '''
    [
    [45, 15, 10, 56, 23],
    [96, 98, 99, 40, 69],
    [96, 84, 49, 46, 34],
    [16, 64, 81, 4, 11],
    [10, 66, 85, 55, 14]
    ]
    '''
    # 모든 요소의 차이 절댓값을 누적시킬 최종 값
    result = 0

    # 2차원 배열의 모든 요소를 순회
    # r은 행의 인덱스, c는 열의 인덱스
    # 첫 for문 2개는 이동을 위한 for문
    for r in range(N):
        for c in range(N):
            # 탐색을 위한 for문
            # 현재 위치 (r, c)의 상하좌우 인접 요소를 확인하기 위한 반복
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 인접한 요소의 좌표가 벽이라면
                if 0 <= nr < N and 0 <= nc < N:
                    # 현재 칸의 값과 인접한 칸의 값의 차이를 구해서 절댓값을 계산
                    result += abs(arr[nr][nc] - arr[r][c])
                else:
                    continue
    print(f'#{tc} {result}')