import sys
sys.stdin = open('5208.txt')

# 최소 충전횟수를 찾는 함수
def find_min_change(cnt, bus_stop):
    global min_cnt
    # 기저 조건: 정류장 5이상 도달 가능(인덱스는 0부터)
    if bus_stop >= N - 1:
        # 최소 비교 후 갱신
        min_cnt = min(min_cnt, cnt)
        return

    # 가지치기: 최소 보다 현재까지의 값이 이미 이상일 때
    if cnt >= min_cnt:
        return
    # 1부터 현재 버스 정류장의 이동 가능 거리 만큼 이동 해봄
    for i in range(1, M[bus_stop] + 1):
        # 충전 횟수 +1, 다음 버스정류장 위치는 bus_stop + i
        find_min_change(cnt + 1, bus_stop + i)


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]
    M = data[1:]
    min_cnt = N - 1
    find_min_change(0, 0)
    # 출발지에서의 배터리 장착은 교환 횟수에서 제외하기 때문에 -1
    print(f'#{tc} {min_cnt - 1}')