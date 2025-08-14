import sys
sys.stdin = open('1224.txt')


# 후위 표기법으로 변경하는 함수
def to_postfix(exp):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = ''
    for token in exp:
        # 1. 피연산자일 경우, 결과에 바로 추가
        if token.isdigit():
            result += token
        # 2. 여는 괄호
        elif token == '(':
            stack.append(token)
        # 3. 닫는 괄호
        elif token == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        # 4. 연산자일 경우, 우선순위 비교
        else:
            while (
                stack
                and stack[-1] != '('
                and precedence.get(stack[-1]) >= precedence.get(token)
            ):
                result += stack.pop()
            stack.append(token)
    # 표현식 순회를 마친후 스택 요소 전부 pop
    while stack:
        result += stack.pop()

    return result


# 후위 표기법 수식 계산
def calculate_postfix(exp):
    stack = []
    for token in exp:
        # 피연산자일 경우
        if token.isdigit():
            stack.append(int(token))
        # 연산자일 경우
        else:
            right = stack.pop()
            left = stack.pop()
            # 연산자에 맞는 계산
            if token == '+':
                result = left + right
            elif token == '*':
                result = left * right

            stack.append(result)

    return stack.pop()


T = 10

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    expression = input()
    postfix = to_postfix(expression)
    final_result = calculate_postfix(postfix)

    print(f'#{tc} {final_result}')