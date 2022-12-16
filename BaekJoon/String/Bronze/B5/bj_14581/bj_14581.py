# https://www.acmicpc.net/problem/14581
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

nickname = input()
fan = ':fan:'
print(fan * 3)
print(f'{fan}:{nickname}:{fan}')
print(fan * 3)