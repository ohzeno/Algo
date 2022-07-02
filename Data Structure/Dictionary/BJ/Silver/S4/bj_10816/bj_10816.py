# https://www.acmicpc.net/problem/10816
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
Counter라는 편한게 collections에 있다곤 하는데...
그냥 딕셔너리에 카운팅했다. 카드 몇장인가 in연산으로 찾을때 O(1)이라 빠름.
"""
n = int(input())
datas = list(input().split())
my = {}
for data in datas:
    if data in my:
        my[data] += 1
    else:
        my[data] = 1
m = int(input())
checks = list(input().split())
ans = []
for check in checks:
    if check in my:
        ans.append(my[check])
    else:
        ans.append(0)
print(*ans)




