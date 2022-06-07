# https://www.acmicpc.net/problem/15841
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == -1:
        break
    """
    8, 9, 10시간에 21, 34, 55
    예제까지 포함해서 보면 피보나치 수열임.
    """
    s1 = 1
    s2 = 1
    for i in range(n - 1):  # 1번째면 s1 그대로, 2번째면 s2가 나오도록 n - 1
        s1, s2 = s2, s1 + s2
    print(f'Hour {n}: {s1} cow(s) affected')
