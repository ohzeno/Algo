# https://www.acmicpc.net/problem/10870
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
n1 = 0  # 0번째 피보나치 수 0
n2 = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:  # 2번째 이상 피보나치
    cur = 2
    while cur <= n:  # n번째까지 반복
        n3 = n1 + n2
        cur += 1
        n1 = n2
        n2 = n3
    print(n3)  # n번째 수 출력



