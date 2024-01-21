# https://www.acmicpc.net/problem/1389
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합
유저 수 N, 친구 관계 수 M
2 <= N <= 100, 1 <= M <= 5000
"""
from collections import deque
n, m = map(int, input().split())
connects = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connects[a].append(b)
    connects[b].append(a)
def bfs(st):
    q = deque([(st, 0)])
    visited = {st}
    costs = {}
    while q:
        cur, d = q.popleft()
        for nxt in connects[cur]:
            if nxt not in visited:
                q.append((nxt, d+1))
                visited.add(nxt)
                costs[nxt] = d+1
    return sum(costs.values())
min_bacon = float('inf')
min_person = -1
for i in range(1, n+1):
    tmp = bfs(i)
    if tmp < min_bacon:
        min_bacon = tmp
        min_person = i
print(min_person)


"""
현 시점 실버 1. 제출 38378. 정답률 	54.808 %
간단한 bfs문제.
태그에 플로이드-워셜이 있는데 그걸로 어떻게 푸는건지 모르겠다.
플로이드-워셜은 거리를 단축하는거고, 이건 거리를 누적해야 한다.
설마 3중 for문 내에서 단축이 아니라 누적을 하고 그걸 플로이드-워셜이라고 한건가?
"""