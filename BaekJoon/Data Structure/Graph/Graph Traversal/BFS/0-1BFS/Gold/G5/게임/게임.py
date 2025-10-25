# https://www.acmicpc.net/problem/1584
import sys
from collections import deque
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
0, 0 -> 500, 500 잃는 생명 최솟값?
위험 구역은 한 칸 움직일 때마다 생명 1씩 잃음.
죽음의 구역은 못 들어감.
"""

mat = [[0]*501 for _ in range(501)]
def get_pos():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return x1, y1, x2, y2
def mapping(n, val):
    for _ in range(n):
        x1, y1, x2, y2 = get_pos()
        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                mat[r][c] = val
mapping(int(input()), 1)  # 위험 구역
mapping(int(input()), -1)  # 죽음의 구역
def bfs_01():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0, 0)])  # 잃는 생명, r, c
    visited = {(0, 0): 0}
    INF = float('inf')
    while q:
        cost, r, c = q.popleft()
        for dr, dc in dirs:
            nx, ny = r + dr, c + dc
            if 0 <= nx <= 500 and 0 <= ny <= 500 and mat[nx][ny] != -1:
                pos = (nx, ny)
                ncost = cost + 1 if mat[nx][ny] == 1 else cost
                if ncost < visited.get(pos, INF):  # 더 적은 생명 잃고 방문했을 경우만
                    if (nx, ny) == (500, 500):
                        return ncost
                    visited[pos] = ncost
                    if ncost == cost:  # 가중치 0이면 앞
                        q.appendleft((ncost, nx, ny))
                    else:  # 가중치 1이면 뒤
                        q.append((ncost, nx, ny))
    return -1
print(bfs_01())


"""
현 시점 Gold V. 제출 3142. 정답률 45.563 %
그냥 bfs하면 시간초과. heap써야 한다.
0-1 bfs 풀이 처음 사용해봤다.
"""
