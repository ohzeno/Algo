# https://www.acmicpc.net/problem/24082
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = int(input())
print(a**3)