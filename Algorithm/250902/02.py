import sys
sys.stdin = open('02.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    # 16진수 입력값
    hex_input = input()
    # 2진수 계산을 위해 입력값의 길이를 저장
    N = len(hex_input)
    # 10진수로 변환 후
    dec_from_hex = int(hex_input, 16)
    # 2진수로 변환(4 * N 자릿수만큼 0을 채워 표시)
    bin_from_dec = format(dec_from_hex, f'0{4 * N}b')

    result = []
    i = 0
    # 2진수를 인덱스로 순회하며
    while i < len(bin_from_dec):
        # 7개씩 잘라
        seven_bits = bin_from_dec[i:i + 7]
        # 7개의 0이 나오면 인덱스를 4칸 뒤로 이동하고 다음 반복 시행
        if seven_bits == '0000000':
            i += 4
            continue
        # 7개의 0이 없다면 10진수로 변환해 결과에 추가, 인덱스를 7증가시킴
        else:
            result.append(int(seven_bits, 2))
            i += 7

    print(f'#{tc}', *result)