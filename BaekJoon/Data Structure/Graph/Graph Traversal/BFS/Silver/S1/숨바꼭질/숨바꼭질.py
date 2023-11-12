# https://www.acmicpc.net/problem/1697
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
from collections import deque
n, k = map(int, input().split())
q = deque()
q.append((n, 0))
visited = set()
visited.add(n)
while q:
    cur, t = q.popleft()
    if cur == k:
        print(t)
        break
    for nxt in [cur-1, cur+1, cur*2]:
        if 0 <= nxt <= 100000 and nxt not in visited:
            q.append((nxt, t+1))
            visited.add(nxt)



"""
현 시점 실버 1. 제출 224336. 정답률 25.530 %
클래스 3에 남은건지 새로 생긴건지 모를 문제가 있어서 풀어봤다.
간단한 bfs 문제.
"""