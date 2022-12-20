# https://www.acmicpc.net/problem/2292
import sys

sys.stdin = open("input.txt")

N = int(input())

n = 1
if N == 1:
    print(1)
else:
    while True:
        if N <= 1 + 6 * (n * (n + 1) / 2):
            print(n + 1)
            break
        else:
            n += 1