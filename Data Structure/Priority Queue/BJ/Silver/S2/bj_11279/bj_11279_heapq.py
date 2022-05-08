# https://www.acmicpc.net/problem/11279

import sys
import heapq

sys.stdin = open("input.txt")

heap = []

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    order = int(sys.stdin.readline().rstrip())
    if order != 0:  # 트리 추가명령
        heapq.heappush(heap, -order)
    else:  # 최대값 출력 후 제거 명령
        if heap:
            print(-heapq.heappop(heap))
        else:  # 배열 비어있을 경우 0 출력
            print(0)
