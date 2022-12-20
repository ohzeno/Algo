# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

sys.stdin = open("input.txt")

dir_x = [0, -1, 0, 1]
dir_y = [1, 0, -1, 0]

def bfs():
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    # 1 전부 큐에 넣기
    for i in range(m):
        for j in range(n):
            if mat[j][i] == 1:
                visited[j][i] = 1
                queue.append((j, i))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            # 큐에서 꺼낸 곳 사방 중에 범위 내이고
            # 방문하지 않은 곳일 때
            if -1 < nx < m and -1 < ny < n and not visited[ny][nx]:
                # 벽이면 방문 음수처리
                if mat[ny][nx] == -1:
                    visited[ny][nx] = -1
                # 덜익은 토마토면 익은 토마토로 교체, 큐에 넣기
                # 방문값은 이전값 +1로 날짜 측정할 수 있게 함
                elif mat[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    mat[ny][nx] = 1
                    queue.append((ny, nx))
    # 덜익은 토마토가 남았으면 -1
    max_p = 0
    for j in range(n):
        for i in range(m):
            if mat[j][i] == 0:
                return -1
            if visited[j][i] > max_p:
                max_p = visited[j][i]
    # 방문행렬 최대값 - 1 = 소요기간
    return max_p - 1


# m은 가로, n은 세로
m, n = map(int, input().split())
# 0: 익지 않은 토마토
# 1: 익은 토마토
# -1: 비어있음
mat = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
