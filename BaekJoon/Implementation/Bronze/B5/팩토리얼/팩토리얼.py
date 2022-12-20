# https://www.acmicpc.net/problem/10872
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
ans = 1
for i in range(n, 1, -1):
   ans *= i
print(ans)