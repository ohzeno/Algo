# https://www.acmicpc.net/problem/14681
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
