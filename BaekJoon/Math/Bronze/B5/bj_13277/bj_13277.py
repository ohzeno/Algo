# https://www.acmicpc.net/problem/13277
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
print(a * b)
