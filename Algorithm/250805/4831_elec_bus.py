'''
현재 갈 수 있는 거리 안에서 최적을 찾는다??????????????????????????
현재 위치에서 갈 수 있는 정류장 중 가장 멀리 떨어진 정류장을 선택
정류장의 종점에서 현재 위치의 거리의 차이가 최대 이동거리보다 작아질 때 반복을 종료함
종점에 도착할 수 없을 때는 0을 출력
'''

import sys
sys.stdin = open('4831.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 최대 이동거리, N: 종점, M: 충전기 수
    K, N, M = map(int, input().split())
    # 충전기 위치 리스트
    arr = list(map(int, input().split()))
    # 충전 횟수
    n_charge = 0
    # 현재 위치
    i_now = 0
    while N - i_now > K:
        # 최대 이동 거리부터 1까지 거리 중 충전기가 있는지
        for i in range(K, 0, -1):
            if i_now + i in arr:
                # 현위치에서 i만큼 이동하고
                i_now += i
                # 충전 횟수 +1
                n_charge += 1
                break
        # 현재 위치 기준 이동할 수 있는 정류장이 없을 경우 0
        else:
            n_charge = 0
            break
    print(f'#{tc} {n_charge}')