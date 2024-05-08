# https://www.acmicpc.net/problem/2252
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
일부 학생들의 키를 비교한 결과가 주어졌을 때, 키 순서대로 줄을 세우는 프로그램을 작성하시오.
1 <= N <= 32,000, 1 <= M <= 10^5
n명, m번 비교
비교 a b는 a가 b보다 앞에 서야 한다는 의미
답이 여럿이면 아무거나 출력.
"""
from collections import deque
def topological_sorting():
    q = deque()
    for i in range(1, n + 1):
        if not enter[i]:
            q.append(i)
    s = []
    while q:
        node = q.popleft()
        s.append(node)
        for next_node in graph[node]:
            enter[next_node] -= 1
            if not enter[next_node]:
                q.append(next_node)
    return ' '.join(map(str, s))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
enter = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    enter[b] += 1
print(topological_sorting())


"""
현 시점 골드 3. 제출 51649. 정답률 57.106 %
위상정렬을 알면 쉽게 풀 수 있는 문제.
"""