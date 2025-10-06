# https://www.acmicpc.net/problem/13777
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
"""

while True:
    n = int(input())
    if n == 0: break
    ll, rr = 1, 50
    elems = []
    while ll <= rr:
        mid = (ll + rr) // 2
        elems.append(mid)
        if mid == n:
            print(*elems)
            break
        if mid < n:
            ll = mid + 1
        else:
            rr = mid - 1


"""
현 시점 Bronze I. 제출 962. 정답률 63.022 %
"""
