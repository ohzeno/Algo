# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def dfs(now):
    for nxt in mat[now]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt)

n = int(input())
c = int(input())
mat = [[] for _ in range(n+1)]
for _ in range(c):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

visited = [0] * (n+1)
visited[1] = 1
dfs(1)
print(sum(visited) - 1)  # 1번 제외한 방문지 = 1번 통해 감염된 컴퓨터 수







