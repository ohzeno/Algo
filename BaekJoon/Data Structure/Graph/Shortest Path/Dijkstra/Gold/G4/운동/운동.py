# https://www.acmicpc.net/problem/1956
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
V개 마을, E개 도로. 도로는 일방 통행.
마을은 1~V번.
시작점으로 돌아오는 사이클. 사이클 도로 길이 합 최소.
두 마을 왕복하는 경우도 사이클.
"""

v, e = map(int, input().split())
# v가 400 제한이고 시간제한이 2초임에도 불구하고 v를 다 순회하면 시간초과가 발생.
# 기존에 주어진 연결그래프를 따로 만들어 연결된 곳만 순회한다.
connects = [[] for _ in range(v + 1)]
costs = [[float('inf')] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    costs[a][b] = c
    connects[a].append((b, c))
q = []
for st in range(1, v + 1):
    # c가 1만 이하이기에 float('inf')인지 체크하지 않고 그냥 넣어도 된다.
    for ed, cost in connects[st]:
        # 유사 다익스트라를 위해 cost가 제일 작은 경우가 앞으로 오도록 heappush
        heappush(q, (costs[st][ed], st, ed))
ans = -1
while q:
    t_cost, st, ed = heappop(q)  # 유사 다익스트라를 위해 cost가 제일 작은 경우를 뽑도록 heappop.
    if st == ed:  # 도착
        ans = t_cost
        break
    if t_cost > costs[st][ed]:
        continue
    for ned, cost2 in connects[ed]:
        n_cost = t_cost + cost2  # st-ed-ned 비용
        if n_cost < costs[st][ned]:
            costs[st][ned] = n_cost
            heappush(q, (n_cost, st, ned))
print(ans)


"""
현 시점 골드4. 제출 17014, 정답률 40.296 %
플로이드 워셜로 풀었고, python3로는 시간초과 발생.
python3로 통과한 풀이를 상당수 살펴봤는데, 전부 heqpq와 다익스트라를 이용한 풀이였다.
플로이드 워셜로는 pypy로 제출해야 할 듯.
다익스트라 풀이도 시도해볼 예정.
순수 다익스트라 풀이는 시간초과가 발생한다. 다익스트라와 bfs를 응용하여 풀었다.
python3로 통과한 기존 풀이들도 다시 살펴보니 다익스트라와 bfs를 응용하였다.
"""