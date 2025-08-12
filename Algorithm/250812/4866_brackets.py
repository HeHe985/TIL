import sys
sys.stdin = open('4866.txt')

T = int(input())

for tc in range(1, T + 1):
    data = input().strip()
    stack = []
    # 스택의 top문자를 저장할 변수
    top_char = ''
    # 입력 문자열을 순회하며
    for i in data:
        # 열림 괄호일 경우 push
        if i in '{(':
            stack.append(i)
        # 닫는 괄호일 경우
        elif i in '})':
            # 스택이 비어있다면 0을 저장하고 반복문을 빠져나감
            if len(stack) == 0:
                result = 0
                break
            # 비어있지 않다면 pop, pop한 문자를 top_char에 저장
            else:
                top_char = stack.pop()
                # pop 이후, 괄호의 짝이 안맞는 경우 0저장, 반복문 빠져나감
                if (i == '}' and top_char != '{') or (i == ')' and top_char !='('):
                    result = 0
                    break
        # 순회중인 문자열이 괄호가 아닐 경우 지나감
        else:
            continue
    # break를 못 만났을 경우
    else:
        # 스택이 비어있다면 1, 비어있지 않다면 0
        if len(stack) == 0:
            result = 1
        else:
            result = 0

    print(f'#{tc} {result}')