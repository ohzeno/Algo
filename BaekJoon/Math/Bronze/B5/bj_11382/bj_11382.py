# https://www.acmicpc.net/problem/11382
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
print(a+b+c)