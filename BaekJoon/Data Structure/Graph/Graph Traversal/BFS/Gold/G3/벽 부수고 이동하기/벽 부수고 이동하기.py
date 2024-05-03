# https://www.acmicpc.net/problem/2206
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
nxm 맵. 0은 이동가능, 1은 벽. 
(1, 1)에서 (n, m)으로 이동하는데 최단거리?
시작 칸과 끝나는 칸도 포함해서 센다.
벽 하나를 부수고 이동해도 된다.
도달 불가하면 -1 출력.
1 <= n, m <= 1000
"""
from collections import deque


def bfs(n, m):
    mat = [list(map(int, list(input()))) for _ in range(n)]
    q = deque([(0, 0, 1, 0)])  # r, c, cnt, 벽 부순 횟수
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]  # [벽 안부수고 방문, 벽 부수고 방문]
    visited[0][0] = [1, 1]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while q:
        r, c, cnt, broke = q.popleft()
        if r == n - 1 and c == m - 1:
            return cnt
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if mat[nr][nc] == 1:
                    if broke == 0 and not visited[nr][nc][1]:
                        visited[nr][nc][1] = 1
                        q.append((nr, nc, cnt + 1, 1))
                elif not visited[nr][nc][broke]:
                    visited[nr][nc][broke] = 1
                    q.append((nr, nc, cnt + 1, broke))
    return -1

n, m = map(int, input().split())
print(bfs(n, m))


"""
현 시점 골드 3. 제출 143524. 정답률 23.341 %
벽 부수기 추가된 bfs.
평범하게 벽을 부쉈는지 안 부쉈는지 여부를 q와 visited 추가하면 된다.
visited에 set를 사용하니 느려서 3차원 배열로 바꿈.
"""
