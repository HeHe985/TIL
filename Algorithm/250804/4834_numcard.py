import sys

sys.stdin = open('input_2.txt')

# 총 테스트케이스 수 만큼 반복
T = int(input())
for tc in range(1, T+1):
    # 카드 장수
    N = int(input())
    # 리스트로 저장
    arr = [int(ch) for ch in input()]
    # 숫자 빈도를 저장할 리스트
    counts = [0] * 10
    # 빈도가 가장 큰 카드의 개수
    cnt_card = 0
    # 가장 많은 카드에 적힌 숫자
    max_card = 0
    # 0부터 9까지와 리스트의 값 비교
    for i in range(10):
        for j in range(N):
            # 리스트의 수가 특정 수과 같다면 그 수의 빈도를 +1
            if i == arr[j]:
                counts[i] += 1
    for n in range(10):
        # 값 갱신
        if cnt_card <= counts[n]:
            cnt_card = counts[n]
            max_card = n

    print(f'#{tc}', max_card, cnt_card)

