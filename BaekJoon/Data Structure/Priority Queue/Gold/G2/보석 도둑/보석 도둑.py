# https://www.acmicpc.net/problem/1202
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
보석 n개.
각 보석은 무게 mi, 가격 vi.
가방 k개. 각 가방 최대 무게 ci.
가방에는 최대 한 개의 보석만 넣을 수 있음.
훔칠 수 있는 보석 가격의 합의 최댓값을 출력.
"""
from heapq import heappush as hpush, heappop as hpop

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort(key=lambda x: x[0])  # 무게 오름차순 정렬. 가치는 아래 hpush, hpop에서 해결된다.
bags.sort()  # 무게 오름차순 정렬
max_price = jewel_idx = 0
available_jewels = []  # 현재 가방에 들어갈 수 있는 보석들
for bag in bags:
    while jewel_idx < n and jewels[jewel_idx][0] <= bag:
        hpush(available_jewels, -jewels[jewel_idx][1])
        jewel_idx += 1
    """
    무게 제한이 낮은 가방부터 순회하므로 
    available에 들어가있는 보석은 현재 가방에도 들어갈 수 있다.
    그 중 가장 비싼 보석을 넣는다.
    """
    if available_jewels:
        max_price += -hpop(available_jewels)
print(max_price)


"""
현 시점 골드 2. 제출 58529. 정답률 22.027%
'훔칠 수 있는 보석의 최대 가격'이라고 적혀있는데 이러면 훔칠 수 있는 보석 중 최고 가격을 의미할 수 있다.
중의적이라 시간낭비를 좀 했다. '훔칠 수 있는 보석 가격의 합의 최댓값'이라고 하면 명확해진다.
무게 제한이 낮은 가방 순으로, 해당 가방에 들어갈 수 있는 보석 중 최대 가격을 넣으면 최적해가 된다.
"""
