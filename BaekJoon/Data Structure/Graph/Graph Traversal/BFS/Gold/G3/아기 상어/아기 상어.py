# https://www.acmicpc.net/problem/16236
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
nxn 공간에 물고기 M마리, 아기 상어 1마리. 한 칸에 물고기 최대 1마리.
아기 상어 초기 크기 2. 상하좌우로 1초에 한칸 이동 가능.
아기 상어는 자신보다 큰 물고기가 있는 칸을 제외하면 이동 가능.
아기 상어는 자신보다 작은 물고기를 먹을 수 있음.
- 더 이상 먹을 수 없는 물고기가 없으면 엄마 상어에게 도움 요청.
- 먹을 수 있는 물고기가 1마리면 그 물고기를 먹으러 감.
- 먹을 수 있는 물고기가 1마리보다 많다면, 가장 가까운 물고기를 먹으러 감.
    - 거리는 아기 상어가 물고기까지 이동하는 칸의 최소 개수.
    - 거리가 가까운 물고기가 많으면 가장 위 물고기, 그래도 여럿이면 가장 왼쪽 물고기 먹음.
물고기 먹는 데 걸리는 시간x.
자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가.
아기 상어가 몇 초 동안 도움 요청 없이 물고기를 잡아먹을 수 있는지 구하라.
0: 빈 칸
1~6: 물고기 크기
9: 아기 상어 위치
"""
from collections import deque


def find_shark():
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 9:
                return i, j


def bfs(x, y, size):
    visited = {(x, y)}
    fishes = []
    q = deque([(x, y, 0)])
    min_d = max_d
    while q:
        x, y, d = q.popleft()
        if d == min_d:  # 최소 거리 먹이만 탐색
            break
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and mat[nx][ny] <= size:
                visited.add((nx, ny))
                if 0 < mat[nx][ny] < size:
                    min_d = d + 1
                    fishes.append((nx, ny))
                    continue  # 먹었으면 더 이동할 필요 없음
                q.append((nx, ny, d + 1))
    return min_d, fishes


n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
max_d = n ** 2
sx, sy = find_shark()
mat[sx][sy] = 0
size, eat, time = 2, 0, 0
while True:
    dist, fishes = bfs(sx, sy, size)
    if not fishes:
        break
    time += dist
    sx, sy = min(fishes)
    mat[sx][sy] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
print(time)


"""
현 시점 골드 3. 제출 70974. 정답률 43.589 %
골드 3 치고는 너무 쉽다. 간단한 bfs를 왜 이렇게 어렵다고 여기는지 모르겠다.
솔직히 실버라고 해도 믿을 듯.
"""
