# https://www.acmicpc.net/problem/5522
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

ans = 0
for _ in range(5):
    ans += int(input())
print(ans)