# https://www.acmicpc.net/problem/2178
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
nxm 크기 미로의 칸에 0 또는 1이 적혀있다.
1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸이다.
(1, 1)에서 출발하여 (n, m)으로 이동할 때 지나야 하는 최소 칸 수를 구하라.
칸을 셀 때는 시작 위치와 도착 위치를 포함한다.
2 <= n, m <= 100
도착할 수 있는 경우만 입력으로 주어진다.
"""
from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
visited = set()
q = deque([(0, 0, 1)])
while q:
    r, c, d = q.popleft()
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nr, nc = r + dx, c + dy
        if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] and (nr, nc) not in visited:
            if nr == n-1 and nc == m-1:
                print(d+1)
                exit()
            q.append((nr, nc, d+1))
            visited.add((nr, nc))


"""
현 시점 실버 1. 제출 187409. 정답률 43.755%
간단한 bfs 문제.
"""