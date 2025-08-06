'''
백지 도화지 배열 10X10을 생성
반복을 돌며 백지가 비어있다면 색칠
비어있지 않다면 보라색 영역 +1
'''

import sys
sys.stdin = open('4836.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 비어있는 백지 배열
    white = [[0]*10 for _ in range(10)]
    # print(white)
    # 겹치는 보라색 영역의 수
    cnt_pupple = 0
    # 칠할 영역의 수만큼 반복을 돌며
    # 빨강은 바로 칠하고, 파랑은 인덱스만 따로 저장
    for n in range(N):
        # 색칠 정보를 저장할 리스트
        info = list(map(int, input().split()))
        # 좌표값과 색상을 각각 저장
        r1 = info[0]
        c1 = info[1]
        r2 = info[2]
        c2 = info[3]
        color = info[4]
        # 행 순환
        for r in range(r1, r2 + 1):
            # 열 순환
            for c in range(c1, c2 + 1):
                # 백지가 비어있다면 색칠
                if white[r][c] == 0:
                    white[r][c] = color
                # 같은 색상의 영역은 겹치지 않으므로 보라색 영역 수 +1
                else:
                    cnt_pupple += 1

    print(f'#{tc} {cnt_pupple}')
