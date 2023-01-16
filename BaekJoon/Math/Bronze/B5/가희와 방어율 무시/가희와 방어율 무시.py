# https://www.acmicpc.net/problem/25238
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
if a * (100 - b) / 100 >= 100:  # 방어율 수치가 100 이상이면 데미지 주지 못한다.
    print(0)
else:
    print(1)
