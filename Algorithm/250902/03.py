import sys
sys.stdin = open('03.txt')

code_info = {
        0: '001101',
        1: '010011',
        2: '111011',
        3: '110001',
        4: '100011',
        5: '110111',
        6: '001011',
        7: '111101',
        8: '011001',
        9: '101111'
    }

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    hex_input = input()
    # 2진수 자릿수 N
    N = 4 * len(hex_input)
    dec_from_hex = int(hex_input, 16)
    bin_from_dec = format(dec_from_hex, f'0{N}b')

    result = []
    i = 0
    # 2진수 문자열의 인덱스를 돌며
    while i < N - 6:
        # 6개씩 자른 후
        six_bits = bin_from_dec[i:i + 6]
        # 코드 정보와 일치하는 지 검사
        for j in range(10):
            # 일치한다면
            if six_bits == code_info[j]:
                # 키 값을 결과에 추가, 인덱스 6증가, break
                result.append(j)
                i += 6
                break
        # 일치하는 값을 못찾아 break가 실행되지 않을 경우 인덱스 1증가
        else:
            i += 1

    print(f'#{tc}', *result)