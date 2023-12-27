# https://www.acmicpc.net/problem/14940
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
지도의 모든 지점에 대해 목표 지점까지의 거리를 구하라
가로, 세로로만 움직일 수 있다.
2 <= N, M <= 1000
0: 갈 수 없는 곳
1: 갈 수 있는 곳
2: 목표 지점
원래 갈 수 없는 땅은 0으로,
갈 수 있는 땅은 거리로
도달할 수 없는 위치는 -1로
"""
from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1] * m for _ in range(n)]

def find_st():
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                ans[i][j] = 0
                q.append((i, j))
                return

q = deque()
find_st()

while q:
    r, c = q.popleft()
    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if mat[nr][nc] == 1 and ans[nr][nc] == -1:
                ans[nr][nc] = ans[r][c] + 1
                q.append((nr, nc))
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            ans[i][j] = 0
for row in ans:
    print(*row)

"""
현 시점 실버 1. 제출 18938. 정답률 37.494 %
평범한 bfs. 목표 지점에서 시작하면 된다.
"""
