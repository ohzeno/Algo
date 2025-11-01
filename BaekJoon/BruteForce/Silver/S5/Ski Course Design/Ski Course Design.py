# https://www.acmicpc.net/problem/9881
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
hills = [int(input()) for _ in range(n)]

min_cost = float('inf')

for low in range(84):
    cost = 0
    high = low + 17
    for h in hills:
        if h < low:
            cost += (low - h) ** 2
        elif high < h:
            cost += (h - high) ** 2
    min_cost = min(min_cost, cost)
print(min_cost)

"""
현 시점 Silver V. 제출 1943. 정답률 46.086 %
스위핑 알고리즘이라고 보고 풀었는데 스위핑이 아니다.
이벤트도 없고 활성 라인 추적도 없다.
브루트포스로 봐야 할 듯.
"""
