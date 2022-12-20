# https://www.acmicpc.net/problem/18301
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
print(int((a + 1) * (b + 1) / (c + 1) - 1))
