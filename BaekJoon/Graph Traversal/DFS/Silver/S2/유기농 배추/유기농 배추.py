# https://www.acmicpc.net/problem/1463
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**4)

"""
상하좌우의 칸은 중앙과 인접해 있다고 취급한다.
배추들이 몇 그룹으로 퍼져있는지 구하라.
"""
def dfs(r, c):
    visited[r][c] = 1
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):  # 인접 칸 탐색
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] and not visited[nr][nc]:
            dfs(nr, nc)  # 범위 이내이고, 배추가 있고, 방문하지 않았다면 탐색

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    mat = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        mat[y][x] = 1
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] and not visited[i][j]:  # 배추가 있고, 방문하지 않았다면
                dfs(i, j)
                cnt += 1  # 배추 그룹 갯수 증가
    print(cnt)


"""
현 시점 실버2. 제출 56144, 정답률 37.549%
전형적인 섬 갯수 구하기 문제.
"""