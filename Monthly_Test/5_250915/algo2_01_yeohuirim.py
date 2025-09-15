# import sys
# sys.stdin = open('algo2_sample_in.txt')

import sys
sys.stdin = open("")
# 최소 이동 거리를 찾는 함수
def find_min_distance(n, distance, position):
    global min_distance
    # 기저조건: 모든 사과를 수확
    if n == N:
        # 마지막에는 (0, 0)창고로 돌아와야 하기에, 마지막 선택했던 좌표에서 창고까지의 거리를 더하고
        distance += abs(data[0][0] - data[position][0]) + abs(data[0][1] - data[position][1])
        # 최솟값 비교후 갱신
        min_distance = min(min_distance, distance)
        return

    # 가지치기: 현재까지 계산한 이동 거리가 이미 기존의 최솟값 이상
    if distance >= min_distance:
        return
    # 1번부터 N번까지(0번은 창고)
    for i in range(1, N + 1):
        # 이미 수확한 사과라면 건너뜀
        if visited[i]:
            continue
        # 현재 선택한 사과를 방문처리
        visited[i] = True
        # 재귀호출로 다음 사과 선택
        find_min_distance(n + 1, distance + abs(data[i][0] - data[position][0]) + abs(data[i][1] - data[position][1]), i)
        # 원상 복귀하고 다음 반복 수행
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 출발지인 창고(0, 0)을 사과의 위치가 저장된 배열의 맨앞에 추가
    data = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
    # 최소 이동 거리를 저장할 min_distance
    min_distance = 200 * (N + 1)
    # 창고가 0번 인덱스이며 그 다음부터는 입력밭은 사과의 위치, 수확했는지 여부를 저장할 visited
    visited = [False] * (N + 1)
    visited[0] = True
    find_min_distance(0, 0, 0)

    print(f'#{tc} {min_distance}')