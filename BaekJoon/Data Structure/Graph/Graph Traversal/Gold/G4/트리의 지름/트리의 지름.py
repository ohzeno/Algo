# https://www.acmicpc.net/problem/1967
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
트리의 지름을 구하는 문제.
각 노드 사이의 거리 중 가장 긴 것이 지름.
노드 수 n: 1~10_000
부모 노드 번호, 자식 노드 번호 오름차순으로 주어짐.
루트 노드는 항상 1. 가중치는 100 이하의 자연수.
"""
from collections import deque

def sol():
    n = int(input())
    if n == 1:
        return 0
    graph = {i: {} for i in range(1, n + 1)}
    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        graph[p][c] = w
        graph[c][p] = w

    def bfs(st):
        max_node = max_d = 0
        visited = {st}
        q = deque([(st, 0)])
        while q:
            cur, d = q.popleft()
            if d > max_d:
                max_node, max_d = cur, d
            for nxt, w in graph[cur].items():
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + w))
        return max_node, max_d

    edge = bfs(1)[0]  # 끝점 하나
    return bfs(edge)[1]  # 끝점에서 가장 먼 거리

print(sol())


"""
현 시점 골드 4. 제출 45331. 정답률 40.913 %
dfs나 bfs로 임의의 노드에서 가장 먼 노드를 찾는다.
그 노드는 100% 지름을 이루는 노드가 된다.
트리를 원형으로 펼치면 임의의 점에서 가장 먼 노드는
항상 트리의 중앙을 거쳐 가장 긴 가지의 끝으로 갈 것이기 때문.
이제 그 끝 노드에서 한 번 더 가장 먼 노드를 찾으면 지름의 반대편 끝이 된다. 
"""
