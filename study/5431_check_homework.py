import sys
sys.stdin = open('5431.txt')

T = int(input())

# for TC: 테스트 케이스 반복문
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    submit_lst = list(map(int, input().split()))
    # 미제출자를 저장할 리스트
    not_submit_lst = []

    # 문제 번호를 순회하며 인풋에 없을 경우 미제출자 리스트에 추가
    for i in range(1, N + 1):
        if i not in submit_lst:
            not_submit_lst.append(i)

    print(f'#{tc}', *not_submit_lst)