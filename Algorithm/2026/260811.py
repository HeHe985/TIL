'''
정보올림피아드
문자 빈도 히스토그램
https://jungol.co.kr/problem/1244
'''


text = ""

for _ in range(4):
    text += input()

cnt = []


for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    cnt.append(text.count(char))

for i in range(max(cnt), 0, -1):
    for j in range(26):
        if cnt[j] >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(" ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
