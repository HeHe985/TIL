import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    doors = list(map(int, input().split()))
    now_position = 0
    cnt = 0
    # 방문했는지 체크할 리스트 chk
    chk = [0] * N
    # 현위치가 마지막 원소가 아니면 계속 반복
    while now_position != N - 1:
        # 현위치가 맨처음(인덱스 0)일 경우
        if now_position == 0:
            # 방문함을 표시, 위치를 우측으로 +1, cnt +1
            chk[now_position] = 1
            now_position += 1
            cnt += 1
        # 현위치가 맨처음이 아니고, 방문했던 위치가 아닐경우
        elif chk[now_position] == 0:
            # 방문표시, 현위치를 인풋 리스트에 들어있는 위치로 이동(인덱스 1 차이남), cnt +1
            chk[now_position] = 1
            now_position = doors[now_position] - 1
            cnt += 1
        # 현위지가 맨처음이 아니고, 방문했던 위치일 경우
        else:
            # cnt +1, 위치를 우측으로 +1
            cnt += 1
            now_position += 1

    print(f'#{tc} {cnt}')