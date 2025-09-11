def solve_nqueens(n):
    """
    N-Queens 문제의 전체 과정을 관리하고 최종 결과를 반환하는 메인 함수.
    """
    solutions = []
    # 각 행에 퀸이 어느 열에 위치하는지 기록하는 리스트.
    # 예: queens[0] = 1 -> 0행 1열에 퀸이 있음
    queens = [-1] * n

    # 0번 행부터 실제 백트래킹 탐색을 시작
    backtrack_helper(n, 0, queens, solutions)

    return solutions


def backtrack_helper(n, row, queens, solutions):
    """
    실제 백트래킹 탐색을 수행하는 재귀 함수 (헬퍼 함수).
    """
    # 기저 조건: 마지막 행(n)까지 퀸을 모두 놓았다면 해를 찾은 것
    if row == n:
        solutions.append(queens[:])  # 현재 퀸 배치를 해답에 추가
        return

    # 재귀 단계: 현재 행(row)의 모든 열(col)에 퀸을 놓아봄
    for col in range(n):
        # 유망성 조사: (row, col)에 퀸을 놓을 수 있는지 확인
        if can_place(queens, row, col):
            # 1. 선택 (Choose): (row, col)에 퀸을 놓음
            queens[row] = col
            # 2. 탐색 (Explore): 다음 행으로 재귀 호출
            backtrack_helper(n, row + 1, queens, solutions)
            # 3. 선택 취소 (Un-choose): 이 문제에서는 다음 for 루프가
            #    queens[row] 값을 덮어쓰므로 별도의 복구 코드는 필요 없음


def can_place(queens, r, c):
    """
    (r, c) 위치에 퀸을 놓을 수 있는지, 이전에 놓았던 퀸들과 비교하여 확인
    """
    # 이전에 놓았던 모든 퀸(i행)들을 확인
    for i in range(r):
        # 같은 열이거나, 대각선에 위치하는지 확인
        # abs(행의 차이) == abs(열의 차이) -> 대각선 관계
        if queens[i] == c or abs(r - i) == abs(c - queens[i]):
            return False
    # 모든 퀸과 충돌하지 않으면 True 반환
    return True


# --- 실행 ---
n = 4
results = solve_nqueens(n)
print(results)
print(f"N={n}일 때, 가능한 해의 개수:", len(results))
