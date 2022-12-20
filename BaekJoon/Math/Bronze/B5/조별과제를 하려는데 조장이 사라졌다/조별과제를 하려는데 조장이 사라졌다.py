# https://www.acmicpc.net/problem/15727
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a = int(input())
b = a // 5  # 몫
c = a - b * 5  # 몫*5 만큼 빼고 남은 수
# c가 1 이상이면 한 번 더 이동해야 하므로 b + 1
if c > 0:
    print(b + 1)
else:
    print(b)