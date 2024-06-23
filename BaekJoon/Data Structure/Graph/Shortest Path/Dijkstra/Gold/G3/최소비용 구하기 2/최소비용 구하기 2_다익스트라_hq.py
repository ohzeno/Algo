# https://www.acmicpc.net/problem/11779
import sys

# sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n(1≤n≤1,000)개의 도시. 한 도시에서 출발, 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스. 
A에서 B까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A에서 B 까지 가는데 드는 최소비용과 경로를 출력하여라. 
항상 시작점에서 도착점으로의 경로가 존재한다.

첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
    출발 도시, 도착 도시, 비용 
    0 ≤ 버스 비용 < 100,000
m+3째 줄에는 구하고자 하는 구간 출발점과 도착점이 주어진다.

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력.
둘째 줄에는 최소 비용 경로에 포함되어있는 도시의 개수를 출력. 출발 도시와 도착 도시도 포함.
셋째 줄에는 최소 비용 경로를 방문하는 도시 순서대로 출력.
"""
from heapq import heappop as hpop, heappush as hpush


def init():
    n, m = int(input()), int(input())
    graph = [{} for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c) if b in graph[a] else c
    st, fin = map(int, input().split())
    return n, m, graph, st, fin


def dijkstra():
    INF = 1e9
    dist = [INF] * (n + 1)
    dist[st] = 0
    p = [-1] * (n + 1)
    q = [(0, st)]
    while q:
        sm_cost, cur = hpop(q)
        if dist[cur] < sm_cost:
            continue
        if cur == fin:
            break
        for ed, me_cost in graph[cur].items():
            new_cost = sm_cost + me_cost
            if new_cost < dist[ed]:
                dist[ed] = new_cost
                p[ed] = cur
                hpush(q, (new_cost, ed))
    return dist, p


def find(p, fin):
    path = []
    while fin != -1:
        path.append(fin)
        fin = p[fin]
    return path[::-1]


n, m, graph, st, fin = init()
dist, p = dijkstra()
path = find(p, fin)
print(dist[fin])
print(len(path))
print(*path)


"""
현 시점 골드 3. 제출 34644. 정답률 36.587 %
우선순위 큐를 사용해봤는데 더 느려졌다. 
시간을 개선하려면 graph를 {k: []}형태가 아니라 [{}]형태로 바꿔서 
중복 간선을 순회하는 시간을 줄여야 한다.

일단 맞힌 사람 python부문 2등과 시간, 코드 길이 격차를 많이 벌리고 1등을 달성하긴 했는데,
그건 이 코드에서 함수 호출을 줄인 코드라 좀 보기 불편하다.
1등한 코드는      136ms 972B, 
이 코드는        144ms 1128B,
2등(다른 사람)은  152ms, 1941B.
"""
