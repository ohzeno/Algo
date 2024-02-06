# https://www.acmicpc.net/problem/1043
import sys
sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()

"""
사람 수 n과 파티 수 m이 주어진다. (1 ≤ n ≤ 50, 0 ≤ m ≤ 50)
이야기의 진실을 아는 사람의 수(0~50)와 번호(1~n)가 주어진다.
이후 각 파티에 오는 사람들 번호가 주어진다.
모든 파티에 참가하면서 들키지 않게 과장된 이야기를 할 수 있는 최대 파티 수를 출력하라.
"""

def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])  # 부모 갱신
    return p[x]

def union(x, y):
    nx, ny = find_parent(x), find_parent(y)
    if nx != ny:
        p[max(nx, ny)] = min(nx, ny)

n, m = map(int, input().split())
tn, *truth = list(map(int, input().split()))
p = list(range(n + 1))
for i in range(1, tn):  # 진실을 아는 사람들을 하나의 집합으로 묶는다.
    union(truth[i - 1], truth[i])
parties = []
for _ in range(m):
    pn, *party = list(map(int, input().split()))
    parties.append(party)
    for i in range(1, pn):  # 파티 사람들 그룹화
        union(party[i - 1], party[i])
# 진실을 아는 사람들의 그룹 넘버
true_group = find_parent(truth[0]) if truth else 0
lies = 0
for party in parties:
    # 모든 파티원이 진실그룹이 아니면 거짓말 할 수 있다.
    if all(find_parent(p) != true_group for p in party):
        lies += 1
print(lies)


"""
현 시점 골드 4. 제출 29061. 정답률 45.029 %
연결그래프로 어떻게 해보려다가 시간복잡도가 너무 커질 것 같아서 union-find로 풀었다.
"""
