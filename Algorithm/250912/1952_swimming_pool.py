import sys
sys.stdin = open('1952.txt')


def find_best_plan(month, cost):
    global min_cost
    # 기저조건: 12달 모두 검사해봤으면 탈출~
    if month > 12:
        min_cost = min(min_cost, cost)
        return
    # 가지치기: 현재 비용이 이미 최솟값 이상이면 탈출
    if cost >= min_cost:
        return

    # 1일권 이용
    find_best_plan(month + 1, cost + plan[month] * day_cost)
    # 1달권 이용
    find_best_plan(month + 1, cost + month_cost)
    # 3달권 이용
    find_best_plan(month + 3, cost + month3_cost)
    # 1년권 이용
    find_best_plan(month + 12, cost + year_cost)


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    day_cost, month_cost, month3_cost, year_cost = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_cost = 3000 * 365

    find_best_plan(1, 0)

    print(f'#{tc} {min_cost}')