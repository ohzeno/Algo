# https://www.acmicpc.net/problem/11650
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = [(tuple(map(int, input().split()))) for _ in range(n)]
datas.sort(key=lambda x: (x[0], x[1]))
for data in datas:
    print(*data)
