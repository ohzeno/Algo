# https://www.acmicpc.net/problem/1167
import sys
sys.setrecursionlimit(int(1e5)+1)
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
트리의 지름을 구하라.
정점 개수 2 <= V <= 100_000
"""
def dfs(node, dist):
    global max_dist, max_node
    if dist > max_dist:
        max_dist = dist
        max_node = node
    visited.add(node)
    for nxt, cost in tree[node].items():
        if nxt not in visited:
            dfs(nxt, dist+cost)

v = int(input())
tree = {i: {} for i in range(1, v+1)}
for _ in range(v):
    a, *data = map(int, input().split())
    for i in range(0, len(data)-1, 2):
        b, cost = data[i], data[i+1]
        tree[a][b] = tree[b][a] = cost
visited = set()
max_dist, max_node = 0, 0
dfs(1, 0)  # 임의의 정점에서 가장 먼 정점 찾기
visited = set()
max_dist = 0
dfs(max_node, 0)  # 가장 먼 정점에서 가장 먼 정점 찾기
print(max_dist)


"""
현 시점 골드 2. 제출 53504. 정답률 33.997 %
코드 지름 구하는 문제. 
이번엔 bfs 사용하지 않고 dfs로 풀어봤다.
스택을 사용하지 않으니 max_dist, max_node를 따로 둬야 해서
좀 난잡해졌다. 그냥 bfs로 푸는게 깔끔한듯.
백준이 채점 기록을 리셋했는지, 내 풀이가 recursionError 처리되어있었다.
베스트 풀이들도 마찬가지. sys.setrecursionlimit으로 해결했다.
주석 내용만 보면 bfs로 이 문제를 풀었던 것 처럼 적혀있는데
폴더에 없는 것을 보면 비슷한 알고리즘 문제를 풀었던 것 같다.
이번엔 bfs도 풀어서 추가했다.
"""