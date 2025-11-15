# https://www.acmicpc.net/problem/4158
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    aset = set()
    for _ in range(n):
        aset.add(int(input()))
    cnt = 0
    for _ in range(m):
        x = int(input())
        if x in aset:
            cnt += 1
    print(cnt)

"""
현 시점 Silver V. 제출 14457. 정답률 25.737 %
이분탐색 태그로 들어왔는데 굳이 이분탐색으로 풀 필요 없는 해시 문제.
정답률이 왜 낮은지 모르겠음.
"""
