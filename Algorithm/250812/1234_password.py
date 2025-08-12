import sys
sys.stdin = open('1234.txt')

T = 10

for tc in range(1, T + 1):
    N, li_str = input().split()
    N = int(N)
    stack = []
    top_char = ''
    for i in li_str:
        # 스택이 비어있다면 현재 요소 push
        if len(stack) == 0 or top_char != i:
            stack.append(i)
            top_char = i
        elif stack.pop == i:
            top_char = stack[-1]
            continue

    print(N, *stack)