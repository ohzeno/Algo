# https://www.acmicpc.net/problem/11265
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def floyd_warshall():
    for tp in range(n_size):  # tp 노드 경유. 출발노드가 아니라 경유노드를 체크.
        for ts in range(n_size):  # ts 노드에서 출발
            for te in range(n_size):  # te 노드로 갈 때
                if ts != tp != te:  # 경유노드가 출발노드나 목적노드와 같으면 안됨.
                    if mat[ts][tp] + mat[tp][te] < mat[ts][te]:  # tp 노드 경유했을 때 더 빠르면 갱신
                        mat[ts][te] = mat[ts][tp] + mat[tp][te]

n_size, n_order = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n_size)]
floyd_warshall()
for i in range(n_order):
    st, ed, time = map(int, input().split())
    if mat[st-1][ed-1] <= time:  # 이내 = 이하
        print('Enjoy other party')
    else:
        print('Stay here')
