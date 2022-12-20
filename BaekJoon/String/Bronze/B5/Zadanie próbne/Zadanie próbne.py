# https://www.acmicpc.net/problem/8545
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

print(input()[::-1])