import sys
sys.stdin = open('1244.txt')


# 넘겨받은 카드 순서로 상금을 계산
def calculate_money(cards):
    sum_money = 0
    for i in range(len(cards)):
        sum_money += cards[i] * 10**(len(cards) - i - 1)
    return sum_money


# 카드를 교환해 최대 순서로 배치하고 그 상금을 계산하는 함수
def find_max_money(arr, cnt):
    global max_money
    # 기저 조건: 최대 탐색횟수(C)번을 완료할 경우 최댓값 갱신 후 리턴
    if cnt == C:
        max_money = max(max_money, calculate_money(arr))
        return
    # 배열의 상태를 저장
    # 교환 횟수별 횟수일 때의 카드 순서를 저장
    # 같은 상태를 만들기 위한 다른 경로를 계산하지 않기 위함
    state = (tuple(arr), cnt)
    # 이미 계산한 경로일 경우 리턴
    if state in visited:
        return
    # 방문 표시
    visited.add(state)
    # 교환할 두 카드를 선택
    for i in range(len(arr)):
        for j in range(len(arr)):
            # 가지치기: 자기 자신과는 교환하지 않음
            if i == j:
                continue
            # 선택한 두 카드를 교환하고 재귀호출
            arr[i], arr[j] = arr[j], arr[i]
            find_max_money(arr, cnt + 1)
            # 카드 원위치
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    info, C = list(input().split())
    # 전처리
    info = list(map(int, info))
    C = int(C)

    max_money = 0
    visited = set()
    find_max_money(info, 0)
    print(f'#{tc} {max_money}')