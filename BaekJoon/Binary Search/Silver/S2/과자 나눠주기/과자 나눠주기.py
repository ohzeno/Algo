# https://www.acmicpc.net/problem/16401
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""
from collections import Counter
# m: 조카 수
# n: 과자 수
m, n = map(int, input().split())
snacks = list(map(int, input().split()))
counter = Counter(snacks)
ll, rr = 1, int(1e9)
possible = 0
while ll <= rr:
    mid = (ll + rr)//2
    cnt = 0
    for k, v in counter.items():
        if k >= mid:
            cnt += k//mid * v
        if cnt >= m:
            break
    if cnt >= m:
        possible = mid
        ll = mid + 1
    else:
        rr = mid - 1
print(possible)


"""
현 시점 Silver II. 제출 17893. 정답률 37.349 %
"""
