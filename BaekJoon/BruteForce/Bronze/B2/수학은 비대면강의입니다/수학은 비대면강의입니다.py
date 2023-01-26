# https://www.acmicpc.net/problem/19532
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

a, b, c, d, e, f = map(int, input().split())
# x = (c * e - b * f) / (a * e - b * d)
# y = c / b - a / b * x
# print(int(x), int(y))
# if not x or not y:
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break

"""
그냥 방정식을 풀면 -999~999를 벗어난 경우, 혹은 분모가 0인 경우가 생긴다.
오히려 무식하게 브루트포스로 풀어야 통과된다...
"""