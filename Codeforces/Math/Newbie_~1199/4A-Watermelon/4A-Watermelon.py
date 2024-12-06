# https://codeforces.com/problemset/problem/4/A
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""
n = int(input())
if n > 2 and n % 2 == 0:
    print("YES")
else:
    print("NO")


"""
현 시점 Difficulty 800. 완료 538084
"""