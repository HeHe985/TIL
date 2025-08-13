import sys
sys.stdin = open('grade_system.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    std_answer = [list(map(int, input().split())) for _ in range(N)]
    # 최고점과 최저점을 저장할 변수
    max_score = 0
    min_score = float('inf')
    # 학생 한명씩 답안을 채점
    for n in std_answer:
        # 채점 점수를 저장할 스택
        stack = []
        # M개의 문항을 검사
        for i in range(M):
            # 정답이며,
            if answer[i] == n[i]:
                # 스택이 비어있거나, 가장 최근에 오답이었을때는 push 1
                if len(stack) == 0 or stack[-1] == 0:
                    stack.append(1)
                # 연속 정답이었을 경우
                else:
                    # 스택의 최근 값을 꺼내 다시 push, 그 값에 +1 한 값을 push
                    num = stack.pop()
                    stack.append(num)
                    stack.append(num + 1)
            # 오답일 경우 push 0
            else:
                stack.append(0)
        # 최고점과 최저점 갱신
        if max_score < sum(stack):
            max_score = sum(stack)
        if min_score > sum(stack):
            min_score = sum(stack)

    result = max_score - min_score

    print(f'#{tc} {result}')