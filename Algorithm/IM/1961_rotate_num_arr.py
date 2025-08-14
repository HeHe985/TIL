import sys
sys.stdin = open('1961.txt')


# 시계방향으로 90도 회전시키는 함수
def rotate90(a, n):
    # 입력받은 배열을 전치시키고
    a_T = list(zip(*a))
    result = []
    # 열 순서를 뒤집음
    rotated_a = [n[::-1] for n in a_T]
    # 출력 형식에 맞춰 한 행씩 join
    for i in rotated_a:
        result.append(''.join(i))
    return result


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    print(f'#{tc}')

    lst_rotate90 = rotate90(arr, N)
    # print(lst_rotate90)

    lst_rotate180 = rotate90(rotate90(arr, N), N)
    # print(lst_rotate180)

    lst_rotate270 = rotate90(rotate90(rotate90(arr, N), N), N)
    # print(lst_rotate270)

    for i in range(N):
            print(lst_rotate90[i], lst_rotate180[i], lst_rotate270[i])