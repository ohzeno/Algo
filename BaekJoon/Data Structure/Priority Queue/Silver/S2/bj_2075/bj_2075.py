# https://www.acmicpc.net/problem/2075
import sys
from heapq import heappop, heapify, heappush
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    mat = list(map(int, input().split()))
    if _ == 0:
        heapify(mat)
        rank = mat  # 첫 n개 원소
    else:
        for ma in mat:
            if ma > rank[0]:  # 새 데이터가 현재 rank의 n번째 큰 원소보다 크면 삽입
                heappush(rank, ma)
                heappop(rank)  # 메모리 초과 해결 위해 rank 원소 큰 순으로 n개 유지하도록 최소값 제거.
print(rank[0])
