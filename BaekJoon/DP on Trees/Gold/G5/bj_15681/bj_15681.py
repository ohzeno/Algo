# https://www.acmicpc.net/problem/15681
import sys
sys.stdin = open('input.txt')
# 최대 10^5개의 노드가 주어지므로 그래프의 최대깊이도 그만큼일 것이라 생각했으나
# count_node는 리프노드에서 한 번 더 들어가므로 +1이 필요하다. 아니면 승수 높이거나.
sys.setrecursionlimit(10**5 + 1)
def input():
    return sys.stdin.readline().rstrip()

def connect_node(st, ed):
    # connect 딕셔너리에 해당 노드가 없으면 생성한 후
    # 연결노드 입력. 무향그래프이므로 양방향 입력한다.
    if st in connect:
        connect[st].append(ed)
    else:
        connect[st] = [ed]
    if ed in connect:
        connect[ed].append(st)
    else:
        connect[ed] = [st]

def count_node(st):
    count[st] = 1  # 자신을 포함하기에 1개로 초기화
    # 모든 연결된 정점에 대해 탐색. 리프노드는 자식이 없으므로 1로 고정됨.
    for child in connect[st]:
        if not count[child]:  # 이미 방문했으면 부모노드다. 자식 노드만 탐색
            count_node(child)  # 자식 노드에 대해 카운트
            count[st] += count[child]  # 자식노드의 카운트를 현재 노드 카운트에 더해준다.

n_node, root, query = map(int, input().split())
connect = {}
for _ in range(n_node - 1):
    a, b = map(int, input().split())
    connect_node(a, b)
count = [0] * (n_node + 1)  # 해당 인덱스를 루트로 하는 서브트리의 노드 수
count_node(root)
for _ in range(query):
    target = int(input())
    print(count[target])



