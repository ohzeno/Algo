# https://www.acmicpc.net/problem/16398
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def find_set(x):
    fn = x
    while p[x] != x:
        x = p[x]
    p[fn] = x  # 최초 원소 부모 갱신. 경로단축. 이거 안하면 시간초과.
    return x

def union(x, y):
    if x == y:
        return
    nx = find_set(x)
    ny = find_set(y)
    p[max(nx, ny)] = min(nx, ny)

def kruskal():
    now_road = 0  # 현재 연결된 간선 수
    total_cost = 0  # 총 비용
    while datas:
        cost, a, b = heappop(datas)
        if find_set(a) != find_set(b):  # 사이클 아니면
            union(a, b)  # 연결
            total_cost += cost  # 비용 추가
            now_road += 1  # 연결 간선 수 갱신
            if now_road == n_stars - 1:  # 간선 수 채웠으면 중단
                break
    return total_cost

n_stars = int(input())
p = [i for i in range(n_stars + 1)]  # 사이클 판별용 유니온파인드 페어런트 리스트
datas = []
for i in range(n_stars):
    costs = list(map(int, input().split()))
    for j in range(n_stars):
        if costs[j]:
            heappush(datas, (costs[j], i, j))  # cost 기준으로 최소힙 정렬되도록
print(kruskal())

