# https://www.acmicpc.net/problem/10815
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
datas = list(map(int, input().split()))
ans = []
for data in datas:
    if data in cards:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)

