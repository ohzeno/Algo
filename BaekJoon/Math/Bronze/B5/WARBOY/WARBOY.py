# https://www.acmicpc.net/problem/26082
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
print(int(3 * b * c / a))

