# https://www.acmicpc.net/problem/14652
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
a = k // m
b = k - a * m
print(f'{a} {b}')
