# https://www.acmicpc.net/problem/15889
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

SAFE = '권병장님, 중대장님이 찾으십니다'
OUT = '엄마 나 전역 늦어질 것 같아'
n = int(input())
soldiers = list(map(int, input().split()))
if n == 1:
    print(SAFE)
    exit()
throwing_ranges = list(map(int, input().split()))
max_reach = throwing_ranges[0]
for i in range(1, n-1):
    if max_reach < soldiers[i]:
        print(OUT)
        exit()
    max_reach = max(max_reach, soldiers[i] + throwing_ranges[i])
if soldiers[-1] <= max_reach:
    print(SAFE)
else:
    print(OUT)


"""
현 시점 Silver III. 제출 2847. 정답률 29.258 %
스위핑 태그 붙어있는데 그냥 그리디다.
"""
