'''
각 버스 정류장을 지나는 노선의 수를 셀 counts 리스트
버스 정류장 번호를 리스트로 변환
주어진 조건(A이상 B이하)을 만족하는 노선을 구해서
만족할 경우 counts의 해당 요소에 +1
'''

import sys
sys.stdin = open('6485.txt')

T = int(input())

for tc in range(1, T+1):
    # 총 버스 노선 수
    N = int(input())
    # N개의 노선 번호 범위 A,B
    list_A, list_B = [], []
    for n in range(N):
        A, B = map(int, input().split())
        list_A.append(A)
        list_B.append(B)
    # 버스 정류장 수
    P = int(input())
    # P개의 C: 버스 정류장 번호
    C = [int(input()) for p in range(P)]

    for i in :


    print(f'#{tc} {counts}')
    # 각 버스 정류장을 지나는 버스 노선의 수

    # counts = [0] * P

    # print(li_AB)