# 1. 범위 안의 좌표만 처리하기
nr = r + dr[i]
nc = c + dc[i]

if 0 <= nr < N and 0 <= nc < M:
    # 여기에 유효한 좌표에 대한 로직을 작성
    print(arr[nr][nc])

# 2. 범위를 벗어나는 좌표는 건너뛰기
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        continue

    # 이 아래는 모두 유효한 좌표임이 보장됨
    print(arr[nr][nc])