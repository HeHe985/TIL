import sys
sys.stdin = open('2005.txt')

T = int(input())

def make_triangle(s, n):
    result_stack = []







for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    stack = [1]
    for n in range(1, N + 1):
        print(stack)
        if n == 2:
            stack.append(1)
        elif n > 2:
            make_triangle(stack)





    # N = int(input())
    # stack = []
    # for n in range(1, N + 1):
    #     triangle = [1] * n
    #     for i in range(n):
    #         if i == 0 or i == n:
    #             continue
    #         else:
    #





        # print(triangle)
