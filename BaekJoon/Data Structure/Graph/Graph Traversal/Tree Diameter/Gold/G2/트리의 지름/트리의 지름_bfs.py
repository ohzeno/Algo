# https://www.acmicpc.net/problem/1167
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

from collections import deque

n = int(input())
graph = {}
for _ in range(n):
    st, *data = map(int, input().split())
    for i in range(0, len(data)-1, 2):
        ed, cost = data[i], data[i + 1]
        graph.setdefault(st, {})[ed] = cost
        graph.setdefault(ed, {})[st] = cost

def bfs(st):
    dist = [-1] * (n + 1)
    dist[st] = 0
    q = deque([st])
    max_dist = max_node = 0
    while q:
        mid = q.popleft()
        for ed in graph[mid]:
            if dist[ed] == -1:
                dist[ed] = dist[mid] + graph[mid][ed]
                q.append(ed)
                if max_dist < dist[ed]:
                    max_dist = dist[ed]
                    max_node = ed
    return max_node, max_dist

node1 = bfs(1)[0]
node2, dist = bfs(node1)
print(dist)



"""
현 시점 Gold II. 제출 65327. 정답률 33.936 %
그래프 2차원배열 사용 -> 메모리 초과
연결그래프 사용.
"""
