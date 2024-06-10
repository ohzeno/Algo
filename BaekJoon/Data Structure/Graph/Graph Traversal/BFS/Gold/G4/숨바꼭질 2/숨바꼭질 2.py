# https://www.acmicpc.net/problem/12851
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.
"""
from collections import deque

def solution(n, k):
    if n >= k:
        return n - k, 1
    times = [False] * (limit + 1)
    q = deque([(n, 0)])
    times[n] = 0
    cnt = 0
    min_time = float('inf')
    while q:
        cur, t = q.popleft()
        if min_time < t:  # 이미 최소 시간을 넘어선 경우
            break
        if cur == k:
            cnt += 1
            min_time = t
            continue
        if min_time == t:  # 목표지 아니고 최소시간이면 다음 탐색 불필요
            continue
        for nxt in (cur - 1, cur + 1, cur * 2):
            # 범위 내에 있고, 아직 방문하지 않았거나 더 이른 시간에 방문한 경우
            if 0 <= nxt <= limit and (not times[nxt] or t + 1 <= times[nxt]):
                times[nxt] = t + 1
                q.append((nxt, t + 1))
    return min_time, cnt

limit = 100_000
n, k = map(int, input().split())
for x in solution(n, k):
    print(x)


"""
현 시점 골드 4. 제출 57693. 정답률 25.619 %
평범한 bfs가 아니라 최소시간으로 방문하는 경로를 세어야 한다.
조금 더러워 졌지만 어려운 로직은 아니다.
정답률이 낮은 이유는 아마 제대로 생각해서 문제를 푸는 사람들이 적어서 그런듯.
익숙한 bfs 풀이를 이해 못하고 외워서 풀던 사람들이 이 문제 만나면 못 풀었을 것.
"""