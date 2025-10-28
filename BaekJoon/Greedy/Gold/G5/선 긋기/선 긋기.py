# https://www.acmicpc.net/problem/2170
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
merged = [data[0]]
for i in range(1, n):
    s, e = data[i]
    if s <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])
print(sum(e-s for s, e in merged))


"""
현 시점 Gold V. 제출 33943. 정답률 36.165 %
스위핑X. 구간병합으로 풀어봤다.
"""
