# https://www.acmicpc.net/problem/1238
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
n개 마을 각각에 한 명의 학생이 살고 있다.
전원이 x번 마을에 모여 파티를 벌이려 함.
1 <= x <= n
이 마을 사이에는 총 m개의 단방향 도로들이 있고 i번째 길을 지나는 데 Ti(1 <= Ti <= 100) 시간이 걸림.
각 학생들은 파티에 참석 후 다시 돌아가야 함.
오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하라.
1 <= n <= 1_000, 1 <= m <= 10_000
"""
from heapq import heappush as hpush, heappop as hpop

n, m, x = map(int, input().split())
connects = {}
for _ in range(m):
    a, b, t = map(int, input().split())
    connects.setdefault(a, []).append((b, t))
mat = {}
for i in range(1, n+1):
    dists = [float('inf')] * (n+1)
    q = [(0, i)]
    while q:
        sm_cost, mid = hpop(q)
        if dists[mid] < sm_cost:
            continue
        for ed, me_cost in connects[mid]:
            new_cost = sm_cost + me_cost
            if new_cost < dists[ed]:
                dists[ed] = new_cost
                hpush(q, (new_cost, ed))
    mat[i] = dists
ans = 0
for i in range(1, n+1):
    if i == x:  # 파티 장소에 사는 사람은 제외
        continue
    ans = max(ans, mat[i][x] + mat[x][i])
print(ans)


"""
현 시점 골드 3. 제출 46144. 정답률 48.539 %
정석 다익스트라는 2번만 사용해야 시간초과가 나지 않는다.
우선순위큐를 사용하면 모든 노드에 대해 다익스트라를 돌리는 것이 가능하다.
"""