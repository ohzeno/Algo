# https://www.acmicpc.net/problem/27433
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

import math
n = int(input())
print(math.factorial(n))
