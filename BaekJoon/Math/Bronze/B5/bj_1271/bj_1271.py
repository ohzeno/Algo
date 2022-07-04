# https://www.acmicpc.net/problem/1271

import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())
print(n // m)
print(n % m)
