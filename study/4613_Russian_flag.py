import sys
sys.stdin = open('4613.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 최솟값 갱신할 변수
    min_cnt = N * M

    # 완전 탐색
    # 흰색이 가질 수 있는 영역
    for w in range(N - 2):
        # 파란색이 가질 수 있는 영역
        for b in range(w + 1, N - 1):
            # 새로 칠해야할 칸 수를 저장할 변수
            cnt = 0

            # 흰색으로 칠할 영역
            for i in range(w + 1):
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1

            # 파란색으로 칠할 영역
            for i in range(w + 1, b + 1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1

            # 빨간색으로 칠할 영역
            for i in range(b + 1, N):
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1

            # 최솟값 갱신
            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{tc} {min_cnt}')