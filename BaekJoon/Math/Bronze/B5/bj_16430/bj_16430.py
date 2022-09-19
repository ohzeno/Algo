# https://www.acmicpc.net/problem/16430
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
print(f'{b - a} {b}')