# https://www.acmicpc.net/problem/24568
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

normal = int(input())
small = int(input())
print(normal * 8 + small * 3 - 28)