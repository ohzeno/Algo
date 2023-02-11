# https://www.acmicpc.net/problem/27294
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

t, s = map(int, input().split())
# 점심이면서 술과 같이 먹지 않는 경우
if not ((12 <= t <= 16) and not s):
    print(280)
else:
    print(320)
