# https://www.acmicpc.net/problem/22193
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = int(input())
b = int(input())
print(a*b)



