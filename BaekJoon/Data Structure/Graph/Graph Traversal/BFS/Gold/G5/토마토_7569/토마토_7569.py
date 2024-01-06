# https://www.acmicpc.net/problem/7569
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
토마토 3차원 배열
보관 후 하루가 지나면 익은 토마토 인접한 곳에 있는 익지 않은 토마토들이 익게 된다.
인접한 곳은 상하좌우앞뒤 6방향
토마토가 스스로 익는 경우는 없다고 가정.
며칠이 지나면 토마토가 모두 익는지, 며칠이 걸리는지 구하라.
칸에 토마토가 없을 수도 있다.
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토가 들어있지 않은 칸
"""
from collections import deque

m, n, h = map(int, input().split())
mat = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dirs = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]


def solution():
    q = deque()
    targets = 0
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if mat[k][j][i] == 1:
                    q.append((i, j, k, 0))
                elif mat[k][j][i] == 0:
                    targets += 1
    if not targets:  # 안익은 토마토가 없는 경우
        return 0
    elif not q:  # 익은 토마토가 없는 경우
        return -1
    day = 0
    while q:
        x, y, z, d = q.popleft()
        if d > day:  # 하루 지난 케이스 들어왔으면 d일째 이미 다 처리됐으니 확인하면 됨.
            if not targets:  # 안익은 토마토가 없으면 d일이 정답
                return d
            day = d  # day 갱신
        for dx, dy, dz in dirs:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and mat[nz][ny][nx] == 0:
                targets -= 1
                mat[nz][ny][nx] = 1
                q.append((nx, ny, nz, d + 1))
    return -1  # 다 돌았는데 안익은 토마토 남아있는 경우


print(solution())


"""
현 시점 골드 5. 제출 82756. 정답률 42.009%
간단한 bfs문제.
dfs로 하면 다음 시작점들 다루는 것이 귀찮다.
"""
