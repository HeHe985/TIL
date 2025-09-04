import sys
sys.stdin = open('4012.txt')


# 음식 시너지를 계산하는 함수
def calculate_synergy(food):
    sum_food = 0
    for i in food:
        for j in food:
            if i == j:
                continue
            sum_food += info[i][j]
    return sum_food


def sum_synergy(cnt, start):
    global min_diff
    # 기저조건: 선택한 개수가 N//2개여야함
    if cnt == N // 2:
        food_A, food_B = [], []
        # N//2개 선택을 완료했을 때
        # 식재료 번호를 하나씩 순회하며
        for i in range(N):
            # A에 선택되었다면 food_A에 append
            if selected_A[i]:
                food_A.append(i)
            # 아니면 B에 추가
            else:
                food_B.append(i)
        # food A/B 리스트를 다 만들었다면 시너지를 계산하여 최솟값 갱신 후 리턴
        min_diff = min(min_diff, abs(calculate_synergy(food_A) - calculate_synergy(food_B)))
        return

    # 재귀 메인 부분
    # 시작 인덱스부터 N전까지 순회하며
    for i in range(start, N):
        # i를 선택하고
        selected_A[i] = True
        # 그 다음 선택을 위해 재귀 호출
        sum_synergy(cnt + 1, i + 1)
        # 돌아오면 A는 원복
        selected_A[i] = False


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    # 음식A에 선택했는지 여부를 나타내는 리스트
    selected_A = [False] * N

    min_diff = float('inf')
    sum_synergy(0, 0)

    print(f'#{tc} {min_diff}')
