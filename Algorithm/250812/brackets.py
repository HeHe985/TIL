import sys
sys.stdin = open('brackets.txt')

T = int(input())

for tc in range(1, T + 1):
    data = input().strip()
    stack = []
    for ch in data:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if len(stack) == 0:
                result = -1
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            result = 1
        else:
            result = -1
    print(f'#{tc} {result}')

