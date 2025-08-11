import sys
sys.stdin = open('1215.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    # 회문수를 셀 변수
    cnt = 0
    str_palin = ''
    # 회문의 길이는 1~8
    for i in range(1, 9):
        # 회문의 길이가 i일 때 행탐색 시작점
        for x in range(9 - i):
            # 열 탐색은 그대로
            for y in range(8):
                str_palin += arr






    print(f'#{tc} {result}')