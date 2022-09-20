# https://www.acmicpc.net/problem/4999
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = input()
b = input()
if len(b) <= len(a):
    print('go')
else:
    print('no')