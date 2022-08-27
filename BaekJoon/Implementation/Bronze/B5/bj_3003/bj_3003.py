# https://www.acmicpc.net/problem/3003
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

k, q, l, b, n, p = map(int, input().split())
print(f'{1-k} {1-q} {2-l} {2-b} {2-n} {8-p}')