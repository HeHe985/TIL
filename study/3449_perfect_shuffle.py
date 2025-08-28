import sys
sys.stdin = open('3449.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    if N % 2 == 1:
        num_harf = N // 2 + 1
    else:
        num_harf = N// 2

    deck1 = arr[:num_harf]
    deck2 = arr[num_harf:]

    print(deck1, deck2)
    




    print(f'#{tc} {result}')