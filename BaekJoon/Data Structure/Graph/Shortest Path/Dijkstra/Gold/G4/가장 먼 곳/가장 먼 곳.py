# https://www.acmicpc.net/problem/22865
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
n개의 땅 중에 a, b, c가 살고있는 집으로부터 가장 먼 곳에 집을 구하려 함.
가장 먼 곳은 선택할 집에서 거리가 가장 가까운 친구의 집까지의 거리를 기준으로 거리가 가장 먼 곳.
1 <= n <= 10_0000
n-1 <= m <= 50_0000
1 <= a, b, c, d, e <= n
1 <= l <= 1_0000
만약 가장 먼 곳이 여러 곳이라면 번호가 가장 작은 땅의 번호를 출력한다.
"""
from heapq import heappush as hpush, heappop as hpop
n = int(input())
costs = [[] for _ in range(n + 1)]
friends = list(map(int, input().split()))
for _ in range(int(input())):
    d, e, l = map(int, input().split())
    costs[d].append([e, l])
    costs[e].append([d, l])
f_dists = []
for friend in friends:
    dists = [float('inf')] * (n + 1)
    dists[friend] = 0
    q = [[0, friend]]
    while q:  # 유사 다익스트라
        mcost, mid = hpop(q)
        if dists[mid] < mcost:  # 이미 코스트가 낮으면 무시
            continue
        for ed, ecost in costs[mid]:
            new_cost = mcost + ecost
            if new_cost < dists[ed]:
                dists[ed] = new_cost
                hpush(q, (new_cost, ed))
    f_dists.append(dists)
tot_max_cost = 0
ans_idx = -1
for pos in range(1, n + 1):
    if pos in friends:
        continue
    cur_min_cost = min(f_dists[0][pos], f_dists[1][pos], f_dists[2][pos])
    if tot_max_cost < cur_min_cost:
        tot_max_cost = cur_min_cost
        ans_idx = pos
print(ans_idx)

"""
현 시점 골드4. 제출 1005, 정답률 33.067%
다익스트라 복습하려고 푼건데 유사 다익스트라를 써야하는 문제였다.
다익스트라로는 뭔짓을 해도 시간초과.
결국 visited도 안쓰고 bfs를 사용하는 유사 다익스트라로 풀었다.
"""

