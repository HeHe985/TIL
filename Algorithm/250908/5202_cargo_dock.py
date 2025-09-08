import sys
sys.stdin = open('5202.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 화물 정보를 종료시간이 빠른 순으로 정렬
    data.sort(key=lambda x: x[1])
    # 이용한 최대 화물차 수
    cnt = 0
    # 큐가 빌 때까지
    while data:
        # 첫 요소를 하나 꺼내 종료시간을 저장하고 cnt +1
        now = data.pop(0)
        end = now[1]
        cnt += 1
        # 큐가 비어있지 않고, 현재 선택한 종료시간보다 큐의 다음 요소의 시작 시간이 같거나 커질때 까지
        while data and end > data[0][0]:
            # 큐에서 꺼내서 버림
            data.pop(0)

    print(f'#{tc} {cnt}')