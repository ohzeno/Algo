# https://www.acmicpc.net/problem/25372
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    if not (6 <= len(input()) <= 9):
        print('no')
    else:
        print('yes')
