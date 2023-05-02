# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def dfs(cur):
    visited[cur] = 1
    print(cur, end=' ')
    for child in mat[cur]:
        if not visited[child]:
            dfs(child)

n, m, st = map(int, input().split())
mat = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)
for i in range(n + 1):
    mat[i].sort()  # 정점 번호 작은 것부터 방문
visited = [0] * (n + 1)
dfs(st)
print()  # 줄바꿈
visited = [0] * (n + 1)  # visited 초기화
q = deque([st])
while q:
    cur = q.popleft()
    if not visited[cur]:
        visited[cur] = 1
        print(cur, end=' ')
        for child in mat[cur]:
            q.append(child)
