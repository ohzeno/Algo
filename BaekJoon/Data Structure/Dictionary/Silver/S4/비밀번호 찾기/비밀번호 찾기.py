# https://www.acmicpc.net/problem/17219
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
"""
n, m = map(int, input().split())
passwords = {}
for _ in range(n):
    site, pw = input().split()
    passwords[site] = pw
for _ in range(m):
    print(passwords[input()])


"""
현 시점 실버4. 제출 14314, 정답률 70.121%
간단한 딕셔너리 문제.
"""