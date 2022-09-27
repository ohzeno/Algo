# https://www.acmicpc.net/problem/8370
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c, d = map(int, input().split())
print(a * b + c * d)
