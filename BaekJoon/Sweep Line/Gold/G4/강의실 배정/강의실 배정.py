# https://www.acmicpc.net/problem/11000
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
events = []
for _ in range(n):
    s, t = map(int, input().split())
    events.append((s, 1))
    events.append((t, -1))
events.sort()
active = 0
max_active = 0
for t, event in events:
    active += event
    max_active = max(max_active, active)
print(max_active)


"""
현 시점 Gold IV. 제출 64504. 정답률 30.298 %
백준은 이상하게 그리디에 스위핑 태그 잔뜩 달고 스위프라인 알고리즘에는 스위핑 안달아놨다.
난이도 기여를 보니 사람들이 스위핑을 생각도 못하고 어렵게 푸는듯.
근데 풀이 코드들을 보면 스위핑 개념을 응용한 풀이가 많다.
"""
