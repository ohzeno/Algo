# https://www.acmicpc.net/problem/11725
import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)  # 안하면 재귀초과로 런타임에러...

def input():
    return sys.stdin.readline().rstrip()


T = int(input())
mat = [[] for _ in range(T+1)]  # 0으로 채우면 메모리 초과하므로 연결노드만 입력
parent = [0] * (T+1)
parent[1] = 1
for _ in range(1, T):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

def dfs(n):
    for ma in mat[n]:  # 연결된 노드 다 탐색
        if not parent[ma]:  # 부모노드 기록 안됐으면 기록 후 dfs
            parent[ma] = n
            dfs(ma)

dfs(1)  # 1번 노드가 루트이므로 1번부터 탐색
for j in range(2, T+1):
    print(parent[j])
