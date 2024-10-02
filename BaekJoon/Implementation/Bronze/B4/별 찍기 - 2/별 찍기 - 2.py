# https://www.acmicpc.net/problem/2439
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)


"""
현 시점 Bronze IV. 제출 348570. 정답률 56.002 %
예전에 풀었는데 레포에는 없어서 다시 풀었다.
"""
