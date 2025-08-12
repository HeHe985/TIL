import sys
sys.stdin = open('4873.txt')

T = int(input())

for tc in range(1, T + 1):
    data = input().strip()
    stack = []
    # 스택의 top 문자
    top_char = ''
    for i in data:
        # 스택이 비어있거나, top 문자와 현재 문자가 다르다면
        if len(stack) == 0 or top_char != i:
            # push 하고 top 문자에 스택의 마지막 요소 할당
            stack.append(i)
            top_char = stack[-1]
        # 스택이 비어있지 않고, top 문자와 현재 문자가 같다면
        else:
            # pop
            stack.pop()
            # pop 이후 빈 스택이 된다면 top 문자에 공백
            if len(stack) == 0:
                top_char = ''
            # 빈 스택이 되지 않는다면 top 문자 재할당
            else:
                top_char = stack[-1]

    print(f'#{tc} {len(stack)}')