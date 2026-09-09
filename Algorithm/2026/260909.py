'''
정보올림피아드
달력
https://jungol.co.kr/problem/1007
'''
# 2000 2 30 
# 2000년 1월 1일은 토요일이다.

def is_leaf(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    y , m, d = map(int, input().split())

    # 1. 입력 검증
    if is_leaf(y):
        month_days[2] = 29
    else:
        month_days[2] = 28
    if d < 1 or m < 1 or m > 12 or y < 2000 or y > 2010 or month_days[m] < d:
        print("INPUT ERROR!")
        continue

    # 2. 경과 총 일수 계산
    total_days = 0
    for year in range(2000, y):
        if is_leaf(year):
            total_days += 366
        else:
            total_days += 365

    for month in range(1, m):
        total_days += month_days[month]

    # 3. 요일 계산
    # 3.1 해당월 1일의 요일
    first_day = (total_days + 6) % 7

    # 3.2 해당일의 요일
    target_day = (first_day + d - 1) % 7


    # 4. 달력 출력
    print(f'{y}. {m}')
    print("sun mon tue wed thu fri sat")

    # 1일이 시작하기 전까지 빈칸 출력
    for _ in range(first_day):
        print("    ", end="")

    # 1일부터 해당 월의 마지막 날짜까지 출력
    for d in range(1, month_days[m] + 1):
        print(f"{d:3}", end=" ")

        # 토요일까지 출력했으면 줄바꿈
        if (first_day + d) % 7 == 0:
            print()

    # 마지막 주가 토요일에 끝나지 않았다면 줄바꿈
    if (first_day + month_days[m]) % 7 != 0:
        print()

    # 5. 요일 출력
    print(days[target_day])
    break

