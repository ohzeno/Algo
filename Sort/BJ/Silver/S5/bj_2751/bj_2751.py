# https://www.acmicpc.net/problem/2751
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = [int(input()) for _ in range(n)]
datas.sort()
for data in datas:
    print(data)
