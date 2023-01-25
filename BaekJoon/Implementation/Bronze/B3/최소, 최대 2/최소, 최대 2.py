# https://www.acmicpc.net/problem/20053
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    datas = list(map(int, input().split()))
    print(min(datas), max(datas))
