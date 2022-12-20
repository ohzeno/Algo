# https://www.acmicpc.net/problem/11022
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')