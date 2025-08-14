import sys
sys.stdin = open('1974.txt')


# 행기준 검사 함수
def is_valid_row(a, n):

    for i in range(n):
        chk_num = [0] * 9
        for j in range(n):
            if j + 1 == a[j]:
                chk_num[j + 1] = 1
        if chk_num.count(1) != 9:
            return False
    return True


# 3X3 칸 검사 함수
def is_valid_subgrid(a, n):
    for i in range(0, 9, 3):




T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    arr_T = list(zip(*arr))
    # print(arr_T)

    valid_row = is_valid(arr, N)
    valid_col = is_valid(arr_T, N)




    # print(f'#{tc} {result}')

'''
행검증, 열검증, 3X3 검증
'''