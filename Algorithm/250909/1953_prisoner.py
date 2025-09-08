import sys
sys.stdin = open('1953.txt')

'''
N: 지하 터널 지도의 세로크기
M: 지하 터널 지도의 가로 크기
R: 맨홀 뚜껑의 세로 위치
C: 맨홀 뚜껑의 가로 위치
L: 탈출 후 소요 시간
data: 지하 터널 지도 정보(0: 터널 없음)
'''
dx = {1: [-1, 1, 0, 0], 2: [-1, 1], 3: [0, 0], 4: [-1, 0], 5: [1, 0], 6: [1, 0], 7: [-1, 0]}
dy = {1: [0, 0, -1, 1], 2: [0, 0], 3: [-1, 1], 4: [0, 1], 5: [0, 1], 6: [0, -1], 7: [0, -1]}
T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)




    # print(f'#{tc} {result}')