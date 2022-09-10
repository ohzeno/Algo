# https://www.acmicpc.net/problem/25304
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

total = int(input())
n = int(input())
pri = 0
for _ in range(n):
    cost, count = map(int, input().split())
    pri += cost * count
if total == pri:
    print('Yes')
else:
    print('No')