# https://www.acmicpc.net/problem/1436
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num = 666
while n:
    if '666' in str(num):
        n -= 1
    num += 1
print(num - 1)
