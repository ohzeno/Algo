# https://www.acmicpc.net/problem/17256
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
# 주어진 조건대로 방정식 세우면 됨.
print(f'{cx - az} {int(cy/ay)} {cz - ax}')
