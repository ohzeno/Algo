# https://www.acmicpc.net/problem/11021
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print(f"Case #{tc}: {a+b}")