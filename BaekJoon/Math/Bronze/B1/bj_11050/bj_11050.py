# https://www.acmicpc.net/problem/11050
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
n, k = map(int, input().split())
"""
조합. nCr = nPr/r!
"""
print(
    int(
        factorial(n)/
        (
                factorial(k) * (factorial(n - k))
        )
    )
)
