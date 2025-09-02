import sys
sys.stdin = open('01.txt')

binary = input()

# 문자열에서 7개씩 건너뛰며 2진수로 변환 및 출력
for i in range(len(binary) // 7):
    print(int(binary[7 * i:7 * i + 7], 2), end=" ")