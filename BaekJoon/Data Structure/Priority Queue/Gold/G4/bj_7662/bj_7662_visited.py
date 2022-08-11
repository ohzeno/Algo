# https://www.acmicpc.net/problem/7662
import sys
from heapq import heappop, heapify, heappush
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def command(com, data, i):
    if com == 'I':
        heappush(minq, (int(data), i))
        heappush(maxq, (-int(data), i))
        visited[i] = 1
    elif com == 'D':
        if data == '1':
            # 큐메 원소가 있고, 삭제된 원소라면 제거
            while maxq and not visited[maxq[0][1]]:
                heappop(maxq)
            # 남아있는 원소가 있으면 최대값 제거하고 visited에서도 제거
            if maxq:
                visited[maxq[0][1]] = 0
                heappop(maxq)
        elif data == '-1':
            while minq and not visited[minq[0][1]]:
                heappop(minq)
            if minq:
                visited[minq[0][1]] = 0
                heappop(minq)

T = int(input())
for _ in range(T):
    visited = [0] * (10 ** 6 + 1)  # 큐에 들어있는지 여부 판별할 리스트
    minq, maxq = [], []
    k = int(input())
    for i in range(k):
        order, num = input().split()
        command(order, num, i)  # 원소 자체는 중복될 수 있기에 i를 인덱스로 활용한다.
    # 큐메 원소가 있고, 삭제된 원소라면 제거
    while minq and not visited[minq[0][1]]:
        heappop(minq)
    if not minq:  # 최소값이 없으면 최대값도 없다.
        print("EMPTY")
    else:
        while maxq and not visited[maxq[0][1]]:
            heappop(maxq)
        print(-maxq[0][0], minq[0][0])
