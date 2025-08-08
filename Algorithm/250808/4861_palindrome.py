'''
1. 크기가 M인 문자열
2. 문자열 역순 정렬
3. 회문인지 검사
'''

import sys
sys.stdin = open('4861.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 행 기준
    for r in range(N):
        for c in range(N - M + 1):
            if arr[r][c:c+M] == arr[r][c:c+M][::-1]:
                result = arr[r][c:c+M]

    # 열 기준
    for c in range(N):
        for r in range(N-M+1):
            c_text = ''
            for m in range(M):
                c_text += arr[r+m][c]
            if c_text == c_text[::-1]:
                result = c_text

    print(f'#{tc} {result}')