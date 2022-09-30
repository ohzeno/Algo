# https://www.acmicpc.net/problem/14928
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
print(int(n%20000303))
