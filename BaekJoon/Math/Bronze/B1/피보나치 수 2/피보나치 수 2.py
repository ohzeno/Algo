# https://www.acmicpc.net/problem/2748
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
def fibonacci(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        n1, n2 = n2, n1 + n2  # 우변의 값은 할당 전에 평가된다. n1 + n2에 n2(n1에 할당된 n2) + n2가 들어갈 일이 없다는 말.
    return n1
print(fibonacci(n))