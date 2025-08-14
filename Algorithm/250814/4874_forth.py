import sys
sys.stdin = open('4874.txt')


# Forth 동작 함수
def forth(exp):
    stack = []
    for token in exp:
        # 토큰이 '.'일 경우 출력
        if token == '.':
            if len(stack) == 1:
                return stack.pop()
            # 스택에 남은 요소가 1개가 아닐 경우
            else:
                return 'error'
        # 토큰이 숫자일 경우
        elif token.isdigit():
            stack.append(int(token))
        # 토큰이 연산자일 경우
        else:
            if stack:
                right = stack.pop()
            else:
                return 'error'
            if stack:
                left = stack.pop()
            else:
                return 'error'

            # 연산자인 토큰에 따라 계산
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left ** right

            # 계산 결과를 다시 push
            stack.append(int(result))


T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    expression = list(input().split())
    final_result = forth(expression)
    print(f'#{tc} {final_result}')
