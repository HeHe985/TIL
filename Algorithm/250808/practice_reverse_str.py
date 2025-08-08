import sys
sys.stdin = open('practice1.txt')

T = int(input())

# for tc in range(1, T + 1):
#     text = list(input())
#     result = []
#     for i in range(len(text) - 1, -1, -1):
#         result.append(text[i])
#     result = ''.join(result)
#     print(f'#{tc} {result}')


for tc in range(1, T + 1):
    text = input()
    result = ''
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    print(f'#{tc} {result}')