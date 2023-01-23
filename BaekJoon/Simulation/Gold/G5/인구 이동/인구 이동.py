# https://www.acmicpc.net/problem/16234
import sys
sys.setrecursionlimit(50 * 51)
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
nxn 크기 땅의 각 칸에 나라가 하나씩 존재. mat[r][c]는 r행 c열에 나라의 인구수
인구 이동은 다음과 같이 진행
- 국경선을 공유하는 두 나라의 인구차가 L~R이면 두 나라 국경선을 연다
- 위의 조건을 만족하는 나라끼리는 연합이라고 한다.
- 연합을 이루고 있는 각 칸의 인구수는 (연합 인구수) / (연합을 이루고 있는 칸의 개수). 소수점은 버림.
- 연합을 해체하고, 모든 국경선을 닫는다.
- 인구 이동이 없을 때까지 위 과정을 반복한다.
각 나라 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하라.
"""
def dfs(r, c):
    visited[r][c] = 1  # 방문처리
    for y, x in dirs:  # 4방향 순회
        nr, nc = r + y, c + x
        # 범위 내이고, 방문하지 않았고, 인구차가 L~R이면
        # 연합 인구에 추가, 연합 좌표에 추가, 재귀.
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if ll <= abs(mat[r][c] - mat[nr][nc]) <= rr:
                total[0] += mat[nr][nc]
                asso.append((nr, nc))
                dfs(nr, nc)

n, ll, rr = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
ans = 0
while True:
    move = 0
    visited = [[0] * n for _ in range(n)]  # visited 초기화
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:  # 방문하지 않은 나라면
                total = [mat[r][c]]  # 연합 인구수
                asso = [(r, c)]  # 연합 좌표들
                dfs(r, c)
                n_asso = len(asso)  # 연합 나라 수
                if n_asso > 1:  # 연합이 존재하면
                    move = 1
                    for y, x in asso:  # 인구 나누기
                        mat[y][x] = total[0] // n_asso
    if move:
        ans += 1  # 인구 이동 날 갱신
    else:  # 연합이 존재하지 않으면 인구 이동X. 종료.
        break
print(ans)

"""
현 시점 골드5. 제출 51106, 정답율 36.258 %
인구 수를 바꾸면서 순회하면 같은 날인지 파악하기 어려울 수 있다. 
하지만 매일 visited를 초기화하기 때문에 이미 수정한 나라가 다른 연합에 이어질 일은 없다.
"""