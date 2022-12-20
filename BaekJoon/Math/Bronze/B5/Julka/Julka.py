# https://www.acmicpc.net/problem/8437
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dif = int(input())
print(n - (n - dif)//2)
print((n - dif)//2)