# https://www.acmicpc.net/problem/14938
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def floyd_warshall():
    for tp in range(1, n_node + 1):  # tp 노드 경유. 출발노드가 아니라 경유노드를 체크.
        for ts in range(1, n_node + 1):  # ts 노드에서 출발
            for te in range(1, n_node + 1):  # te 노드로 갈 때
                if ts != tp != te:  # 경유노드가 출발노드나 목적노드와 같으면 안됨.
                    if mat[ts][tp] + mat[tp][te] < mat[ts][te]:  # tp 노드 경유했을 때 더 빠르면 갱신
                        mat[ts][te] = mat[ts][tp] + mat[tp][te]
def solution():
    floyd_warshall()
    ans = 0
    for i in range(1, n_node + 1):
        tmp = items[i]  # 출발 노드 아이템 추가
        for j in range(1, n_node + 1):
            if i != j:  # 출발 노드 자신으로의 경로는 체크하지 않음
                cost = mat[i][j]
                if cost <= search_scope:  # 탐색범위 이내이면
                    tmp += items[j]  # 아이템 추가
        if tmp > ans:  # 현 출발 노드에서의 아이템이 기존 최대값보다 크면 갱신
            ans = tmp
    return ans  # 최대값 리턴

n_node, search_scope, n_road = map(int, input().split())
items = [0] + list(map(int, input().split()))
mat = [[float('inf')] * (n_node + 1) for _ in range(n_node + 1)]
for _ in range(n_road):
    a, b, cost = map(int, input().split())
    mat[a][b] = cost  # 쌍방 코스트 갱신
    mat[b][a] = cost
print(solution())


