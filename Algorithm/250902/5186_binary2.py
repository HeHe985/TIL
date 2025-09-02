import sys
sys.stdin = open('5186.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    dec_data = float(input())

    result = ''
    # -1 ~ -13 차례로 돌며
    for i in range(-1, -13, -1):
        # 2의 i제곱 보다 같거나 클경우 1
        if dec_data >= 2**i:
            dec_data -= 2**i
            result += '1'
            # 단, 0일경우는 바로 반복문을 빠져나감
            if dec_data == 0:
                break
        # 2의 i제곱 보다 작을 경우 0
        elif dec_data < 2**i:
            result += '0'

    # for문을 다 돌고 나서도 0보다 큰 수가 남았다면 오버플로우
    if dec_data > 0:
        result = 'overflow'

    print(f'#{tc} {result}')