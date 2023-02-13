# https://www.acmicpc.net/problem/27434
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

import math
print(math.factorial(int(input())))
