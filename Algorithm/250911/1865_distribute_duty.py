import sys
sys.stdin = open('1865.txt')


def max_success_probability(row, prob, selected):
    global max_prob

    # 기저조건: 모든 직원에 대해 일을 분배했을 때
    if row == N:
        max_prob = max(max_prob, prob)
        return

    # 가지치기: 현재까지의 확률이 이미 최대 확률보다 작으면 종료(더 커질 일 없음)
    if prob <= max_prob:
        return

    # 모든 업무를 하나씩 맡겨봄
    for i in range(N):

        # 이미 다른 직원이 맡은 업무면 종료
        if selected[i]:
            continue

        # 방문처리
        selected[i] = True
        # 다음 직원 업무 할당
        max_success_probability(row + 1, prob * probability[row][i]/100, selected)
        # 원상 복귀
        selected[i] = False


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    probability = [list(map(int, input().split())) for _ in range(N)]

    max_prob = 0
    selected = [False] * N
    max_success_probability(0, 1, selected)

    print(f'#{tc} {max_prob * 100:.6f}')