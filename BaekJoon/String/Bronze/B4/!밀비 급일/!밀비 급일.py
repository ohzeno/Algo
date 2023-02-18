# https://www.acmicpc.net/problem/11365
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == 'END':
        break
    print(s[::-1])