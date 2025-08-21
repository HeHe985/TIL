import itertools
import sys
sys.stdin = open('baby_gin.txt')

# 3장 연속 숫자: run
# 3장 동일 숫자: triplet
# 6장 run&triplet 구성: baby-gin


# run 검사
def check_run(a):
    cnt = 0
    if a[0] + 1 == a[1] and a[0] + 2 == a[2]:
        cnt += 1
    return cnt


# triplet 검사
def check_triplet(a):
    cnt = 0
    if a[0] == a[1] and a[0] == a[2]:
        cnt += 1
    return cnt


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    cards = list(map(int, input().strip()))
    # 인덱스 선택용 0 ~ 5 리스트
    cards_idx = [i for i in range(6)]
    # 카드 인덱스의 순열 리스트
    deck_idx = list(itertools.permutations(cards_idx, 6))

    # 각 순열 조합을 순회
    for d in deck_idx:
        # 0~2 / 3~5
        deck1 = [cards[d[i]] for i in range(0, 3)]
        deck2 = sorted([cards[d[i]] for i in range(3, 6)])

        # 함수를 호출하여 런, 트리플렛 계산
        run1 = check_run(deck1) + check_run(deck2)
        triplet = check_triplet(deck1) + check_triplet(deck2)

        # 베이비 진 만족하면 브레이크
        if run1 + triplet == 2:
            result = 'true'
            break
        else:
            result = 'false'

    print(f'#{tc} {result}')
