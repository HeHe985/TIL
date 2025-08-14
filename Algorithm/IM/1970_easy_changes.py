import sys
sys.stdin = open('1970.txt')

T = int(input())
cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    changes = [0] * 8
    N = int(input())
    for i in range(8):
        # 거슬러 줘야할 금액을 현금 단위 별로 나눠 몫을 저장
        cnt_cash = N // cash[i]
        # 거슬러 준만큼 앞으로 줘야할 금액에서 뺌
        N -= cnt_cash * cash[i]
        # 거스름돈 단위별 개수를 저장하는 리스트에 몫 저장
        changes[i] = cnt_cash

    print(f'#{tc}')
    print(*changes)