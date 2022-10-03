# https://www.acmicpc.net/problem/20254
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c, d = map(int, input().split())
print(56 * a + 24 * b + 14 * c + 6 * d)