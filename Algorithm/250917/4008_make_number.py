import sys
sys.stdin = open('4008.txt')

# 계산기 함수
def calculate(operator, num1, num2):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator == 2:
        return num1 * num2
    elif operator == 3:
        return int(num1 / num2)


def dfs(idx, answer):
    global max_answer, min_answer

    # 기저조건: 인덱스가 N - 1도달시 최대/최소 갱신후 종료
    if idx == N - 1:
        max_answer = max(max_answer, answer)
        min_answer = min(min_answer, answer)
        return

    # 연산자 4개 검사하며 값이 0이 아닐때 하나씩 사용하고 사용처리
    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            # 재귀 호출로 다음 연산자 선택 및 계산
            dfs(idx + 1, calculate(i, answer, numbers[idx + 1]))
            # 원상 복귀
            opers[i] += 1


T = int(input())
# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_answer = -100000000
    min_answer = 100000000
    opers = operators.copy()

    dfs(0, numbers[0])

    print(f'#{tc} {max_answer - min_answer}')