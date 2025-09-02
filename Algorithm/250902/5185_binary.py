import sys
sys.stdin = open('5185.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, hex_num = input().split()
    result = []
    # 16진수 문자열 한글자 마다
    for i in hex_num:
        # 4비트의 2진수로 변환후 결과에 저장
        result.append(format(int(i, 16), '04b'))

    print(f'#{tc}', ''.join(result))