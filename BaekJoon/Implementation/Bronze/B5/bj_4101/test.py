# https://www.acmicpc.net/problem/4101
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')