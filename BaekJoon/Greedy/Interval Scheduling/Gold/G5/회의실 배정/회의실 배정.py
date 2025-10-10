# https://www.acmicpc.net/problem/1931
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
한 개의 회의실을 이용하려는 n개의 회의에 대해 사용표를 만들려 한다.
각 회의 i에 대해 시작, 끝 시간이 주어져 있고,
각 회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수를 찾아라.
희의의 시작과 끝이 같을 수도 있다.
1 <= n <= 100,000
0 <= 시작 시간 <= 끝 시간 <= 2^31 - 1
"""
n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = st = ed = 0
for mst, med in meetings:
    if ed <= mst:
        cnt += 1
        ed = med
print(cnt)


"""
현 시점 골드 5. 제출 197324. 정답률 30.271 %
Interval Scheduling. x[1]로 정렬.
예전에 많이 풀었던 종류의 문제인데 오랜만에 보니 잘 생각나지 않아서 st기준으로 먼저 정렬했었다.
key로 x[1]만 사용하면 4 4, 0 4의 경우 4 4가 먼저 오게 되어서 오류가 생긴다.
(4 4를 먼저 채택하면 ed(4) > mst(0)이라 0, 4를 사용하지 못한다) 
그래서 x[0]도 같이 정렬해줘야 한다.
"""
