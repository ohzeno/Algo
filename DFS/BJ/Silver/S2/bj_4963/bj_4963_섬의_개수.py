# https://www.acmicpc.net/problem/4963
import sys

# 재귀 깊이 문제로 오류나는거 해결
sys.setrecursionlimit(10000)
sys.stdin = open("input.txt")

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 1, 0, -1, 1, 0, -1]

def dfs(y, x):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 위치가 맵 안이고, 땅이고, 방문하지 않은 곳이면 방문처리 후 dfs.
        # 이렇게 돌면 섬 하나 통째로 방문처리됨.
        if 0 <= nx < w and 0 <= ny < h and \
                not visited[ny][nx] and mat[ny][nx] == 1:
            visited[ny][nx] = 1
            dfs(ny, nx)
    return

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 1은 땅, 0은 바다
    mat = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    land = 0
    for i in range(w):
        for j in range(h):
            # 모든 장소 돌며 땅이고 아직 방문 안한 장소면 방문처리 후 dfs, 섬 갯수 추가
            if mat[j][i] == 1 and not visited[j][i]:
                visited[j][i] = 1
                dfs(j, i)
                land += 1
    print(land)



