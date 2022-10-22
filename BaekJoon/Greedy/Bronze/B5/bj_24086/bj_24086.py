# https://www.acmicpc.net/problem/24086
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = int(input())
print(int(input()) - a)
