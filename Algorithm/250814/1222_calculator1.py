import sys
sys.stdin = open('1222.txt')


# 후위 표기법 수식 계산
def calculate_postfix(exp):
    stack = []
    for token in exp:
        # 피연산자일 경우
        if token.isdigit():
            stack.append(token)
        # 연산자일 경우
        else:
            right = int(stack.pop())
            left = int(stack.pop())

            result = left + right

            stack.append(result)

    return stack.pop()


T = 10

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    expression = input()
    # 더하기 기호의 개수를 셈
    cnt_plus = expression.count('+')
    # 표현식에서 더하기 기호를 모두 지운 다음
    postfix = list(expression.split('+'))
    # 맨뒤에 더하기 기호의 개수만큼 추가
    postfix.extend(['+'] * cnt_plus)
    final_result = calculate_postfix(postfix)

    print(f'#{tc} {final_result}')