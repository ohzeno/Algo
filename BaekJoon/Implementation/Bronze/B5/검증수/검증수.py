# https://www.acmicpc.net/problem/2475
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

nums = list(map(int, input().split()))
acc = sum([i**2 for i in nums])
print(acc % 10)

"""
현 시점 Bronze V. 제출 77476. 정답률 74.633 %
예전에 풀었는데 레포에는 없어서 다시 풀었다.
"""
