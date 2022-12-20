# https://www.acmicpc.net/problem/20492
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = int(input())
print(f'{int(a * 0.78)} {int(a * (1 - (0.2 * 0.22)))}')
