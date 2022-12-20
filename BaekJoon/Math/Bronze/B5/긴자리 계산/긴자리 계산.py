# https://www.acmicpc.net/problem/2338
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)