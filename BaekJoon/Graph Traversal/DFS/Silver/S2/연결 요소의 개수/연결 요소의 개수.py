# https://www.acmicpc.net/problem/11724
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**4)
"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
"""
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 섬찾기면 양방향이어야 함. 아래 주석참고
visited = [0] * (n+1)

def dfs(cur):
    visited[cur] = 1
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
"""
현 시점 실버2. 제출 93634, 정답률 42.414%
연결 요소의 정의도 안적혀있고 간선이 단방향인지 양방향인지도 안적혀있다. 
많이 불친절한 문제.
예제를 분석해보니 사이클 찾기로 보였다. 
component라고 하면 노드 하나를 의미하는 것 같은데
connected component는 그래프 이론에서 연결된 그룹을 의미하는 용어인 듯 하다.
1 2 5 1 이 사이클인 경우, 단방향이면 1에서 dfs를 돌리면 1 2 5만 방문처리가 된다.
3->5가 있는 경우 3에서 다시 cnt가 증가되는데 3은 하나의 사이클이 아니므로 제외해야 한다.
그래서 양방향으로 추정했고, 단방향, 양방향 모두 제출해봤다.
단방향으로 제출하면 틀리는 케이스가 나온다.
"""