import sys
sys.stdin = open('5209.txt')


def find_min_cost(row, cost, selected):
    global min_cost

    # 기저조건: 모든 제품을 어느 공장에서 생산할지에 대한 선택을 마쳤을 경우
    if row == N:
        min_cost = min(min_cost, cost)
        return

    # 가지치기: 현재 비용이 이미 최소값을 넘는다면 종료
    if cost >= min_cost:
        return

    for i in range(N):
        # 이미 선택한 열이면 건너뜀
        if selected[i]:
            continue
        # i열 선택
        selected[i] = True
        # 다음 행 검사
        find_min_cost(row + 1, cost + V[row][i], selected)
        # 원상 복귀
        selected[i] = False


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    # 공장이 선택 됐는지 담고있는 방문 검사 리스트
    selected = [False] * N
    min_cost = 99 * N * N
    find_min_cost(0, 0, selected)

    print(f'#{tc} {min_cost}')