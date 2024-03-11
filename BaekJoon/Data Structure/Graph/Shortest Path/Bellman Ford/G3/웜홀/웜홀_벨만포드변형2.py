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
    dist = [0] * (n + 1)
    cur_nodes = range(1, n + 1)
    for i in range(n):
        nxt_nodes = []
        for mid in cur_nodes:
            for ed, me_cost in graph[mid]:
                if (new_cost := dist[mid] + me_cost) < dist[ed]:
                    dist[ed] = new_cost
                    nxt_nodes.append(ed)
        if not nxt_nodes:
            return False
        cur_nodes = nxt_nodes
    return True


def solution():
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    if bellman_ford(n, graph):
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solution())


"""
현 시점 골드 3. 제출 50347. 정답률 21.485 %
벨만 포드 알고리즘 변형.

그나마 귀납증명과 비슷한 로직을 사용하도록 바꿔봤다.
"""
