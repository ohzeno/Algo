# https://www.acmicpc.net/problem/2170
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
events = []
for _ in range(n):
    s, e = map(int, input().split())
    events.append((s, 1))
    events.append((e, -1))
events.sort()
active = 0
prev = 0
total = 0
for idx, event in events:
    if active > 0:
        total += idx - prev
    active += event
    prev = idx
print(total)


"""
현 시점 Gold V. 제출 33943. 정답률 36.165 %
일반 스위핑.
"""
