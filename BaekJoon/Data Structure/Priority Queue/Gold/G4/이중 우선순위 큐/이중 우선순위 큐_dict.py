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
    elif com == 'D':
        if data == '1':
            # 큐에 원소가 있고, 최대값이 삭제된 원소면 제거
            while maxq and maxq[0][1] in delist:
                heappop(maxq)
            # 큐에 원소가 남아있으면 최대값 제거하고 딕셔너리에 기록
            if maxq:
                delist[heappop(maxq)[1]] = 1
        elif data == '-1':
            while minq and minq[0][1] in delist:
                heappop(minq)
            if minq:
                delist[heappop(minq)[1]] = 1

T = int(input())
for _ in range(T):
    delist = {}  # 삭제된 원소 기록할 딕셔너리
    minq, maxq = [], []
    k = int(input())
    for i in range(k):
        order, num = input().split()
        command(order, num, i)  # 원소 자체는 중복될 수 있기에 i를 인덱스로 활용한다.
    min_n = 0
    while minq:
        tmp = heappop(minq)
        if not tmp[1] in delist:
            # 꺼낸 값이 삭제원소에 없으면 최소값임.
            min_n = tmp
            break
    if not min_n:  # 최소값이 없으면 최대값도 없다.
        print("EMPTY")
    else:
        while maxq:
            tmp = heappop(maxq)
            if not tmp[1] in delist:
                max_n = tmp
                break
        print(-max_n[0], min_n[0])
