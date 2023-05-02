# https://www.acmicpc.net/problem/1005
from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
매 게임 시작 시 건물 짓는 순서가 주어진다. 각 건물에 건설시간이 존재한다.
건물 번호는 1~n
1번 이후 2, 3이 있다면 2, 3을 동시에 건설 진행 가능.
4번 전에 2, 3이 있다면 2, 3이 모두 완성되어야 4번 건설을 시작할 수 있음.
매 경기에서 특정 건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내라.
"""
def topological_sorting():
    q = []
    for node in range(1, n + 1):
        if not enter[node]:  # 진입차수가 0인 노드 넣기
            hpush(q, (times[node], node))  # 시간이 짧은 순으로 정렬되도록 시간을 앞으로.
    while q:
        time, node = hpop(q)
        ans[node] = time  # 해당 건물 최소 시간 기록
        for next in nexts[node]:  # 현재 건물이 선행 건물인 건물들 탐색
            enter[next] -= 1  # 진입 차수 줄여줌
            if not enter[next]:  # 진입 차수가 0이라면 q에 넣는다.
                if next == w:  # 목표 건물이라면
                    ans[w] = time + times[next]  # 목표 건물 최소 시간 기록
                    return  # 종료
                hpush(q, (time + times[next], next))  # 누적시간과 함께 다음 건물 큐에 넣기

hpush, hpop = heappush, heappop
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))  # 건설 소요 시간
    nexts = [[] for _ in range(n + 1)]  # 선행 건설 정보
    enter = [0] * (n + 1)  # 진입 차수
    ans = [0] * (n + 1)  # 각 건물 최소 시간
    for _ in range(k):
        a, b = map(int, input().split())
        nexts[a].append(b)  # a가 b의 선수 건물
        enter[b] += 1  # b 진입 차수 업데이트
    w = int(input())  # 목표 건물
    topological_sorting()
    print(ans[w])

"""
현 시점 골드3. 제출 61025, 정답률 26.743%
단순 위상정렬은 아니고, 약간의 응용이 필요하다. 
1-(2,3)-4인 경우 2, 3이 동시에 진행되지만 시간은 2, 3중 더 오래걸리는 시간이 누적된다.
4번에 진입할 때 차수를 2에서 먼저 깎지만 4의 진입 차수 1이 남아 기록되지 않는다.
3에서 4로 넘어갈 때 4의 진입차수가 0이 되기에 3의 시간만 누적되게 된다.
그러니 시간이 짧은 쪽에 먼저 진입하여, 큰 쪽이 누적되도록 heapq를 사용했다.
위상정렬도 오랜만이라 알고리즘을 완전히 잊고 있었기에 한 번 개념을 훑어보고 풀었다.
"""