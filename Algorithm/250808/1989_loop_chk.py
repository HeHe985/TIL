'''

'''

import sys
sys.stdin = open('1989.txt')

T = int(input())

def reverse_text(s):
    reversed_text = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_text += s[i]
    if s == reversed_text:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    text = input()
    result = reverse_text(text)
    print(f'#{tc} {result}')