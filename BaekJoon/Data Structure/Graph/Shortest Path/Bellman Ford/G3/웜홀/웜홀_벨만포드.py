# https://www.acmicpc.net/problem/1865
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n개 노드. m개 도로와 w개 웜홀.
도로는 양방향, 웜홀은 단방향.
웜홀을 지나면 시간이 되돌아감.
출발점으로 돌아왔을 때, 출발 시각보다 이전인 경우가 있는지 구하라.
1 <= n <= 500
1 <= m <= 2500
1 <= w <= 200
0 <= t <= 10_000
"""


def bellman_ford(n, graph):
    dist = [INF] * (n + 1)
    dist[0] = 0
    for i in range(n+1):
        for mid in graph:
            if dist[mid] == INF:
                continue
            for ed, me_cost in graph[mid]:
                if (new_cost := dist[mid] + me_cost) < dist[ed]:
                    if i == n:
                        return True
                    dist[ed] = new_cost
    return False

def solution():
    n, m, w = map(int, input().split())
    graph = {}
    for i in range(m):
        s, e, t = map(int, input().split())
        graph.setdefault(s, []).append((e, t))
        graph.setdefault(e, []).append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.setdefault(s, []).append((e, -t))
    for i in range(1, n+1):
        graph.setdefault(0, []).append((i, 0))
    if bellman_ford(n, graph):
        return "YES"
    return "NO"

INF = 2500 * 2 * 10_000
for _ in range(int(input())):
    print(solution())


"""
현 시점 골드 3. 제출 50347. 정답률 21.485 %
벨만 포드 알고리즘.

이해하기 편하게 노드 추가하고 원본 벨만포즈로 구현했다.
"""
