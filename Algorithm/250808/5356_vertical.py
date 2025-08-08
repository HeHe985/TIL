'''

'''

import sys
sys.stdin = open('5356.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    result = ''
    # 행우선 순회
    for c in range(15):
        # 열 순회
        for r in range(5):
            # 열의 인덱스가 현재 행의 문자열 크기 이내일때
            if c < len(arr[r]):
                result += arr[r][c]
            else:
                # 범위 밖일때는 건너뛰기
                continue

    print(f'#{tc} {result}')
