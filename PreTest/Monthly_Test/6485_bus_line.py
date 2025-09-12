import sys
sys.stdin = open('6485.txt')

'''
N: 버스 노선 개수
data: [A, B] i번째 버스 노선은 A이상 B이하의 모든 버스정류장을 다님
P: 버스 정류장 수
C: j번 버스 정류장 번호
'''

T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    # 버스 정류장 정보 저장할 리스트(0 패딩)
    counts = [0] * P
    # [A, B] 한세트씩 검사
    for i in data:
        # 해당하는 정류장 개수를 세어줌
        for j in range(P):
            if i[0] <= C[j] <= i[1]:
                counts[j] += 1

    print(f'#{tc}', *counts)

    # # 출력 결과를 저장할 리스트
    # result = []
    # # C로 주어진 정류장 번호에 해당하는 정류장의 노선수만 추가
    # for k in range(P):
    #     result.append(bus_stop[C[k]])

    # print(f'#{tc}', *result)