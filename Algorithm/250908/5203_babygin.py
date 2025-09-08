import sys
sys.stdin = open('5203.txt')


# run 검사
def is_run(card):
    card = sorted(card)
    if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
        return True


# triplet 검사
def is_triplet(card):
    if card[0] == card[1] == card[2]:
        return True


# 뽑은 카드 중 3개를 고르는 함수
def choice_three(cnt, cards, start, deck):
    # 3개를 다 뽑으면 런/트리플렛 검사 후 해당하면 1 반환, 아니면 0반환
    if cnt == 3:
        if is_run(deck) or is_triplet(deck):
            return 1
        return 0
    # 인자로 받은 카드 수 만큼 반복을 돌며 하나씩 카드 덱에 추가
    for i in range(start, len(cards)):
        deck.append(cards[i])
        # 재귀 호출과 동시에 반환값이 1이면 바로 1반환
        if choice_three(cnt + 1, cards, i + 1, deck) == 1:
            return 1
        deck.pop()
    # 아무것도 아닐 때 0반환
    return 0


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    player1, player2 = [], []
    result = 0

    # 1번 2번 플레이어 카드 나눠줌
    for i in range(12//2):
        player1.append(data[2*i])
        player2.append(data[2*i + 1])
        # 플레이어 1이 3장 받았을 때 부터 검사
        if i >= 2:
            # 런/트리플렛 일 경우 1을 반환하기 때문에 먼저 검사했을때 반환값이1이면 1번 플레이어 우승
            if choice_three(0, player1, 0, []) == 1:
                result = 1
                break
            # 1번 플레이어 검사 후 2번 플레이어 검사시 런/트리플렛일 경우 2번 우슨
            elif choice_three(0, player2, 0, []) == 1:
                result = 2
                break

    print(f'#{tc} {result}')