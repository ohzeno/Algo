# https://www.acmicpc.net/problem/11265
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def floyd_warshall():
    for i in range(n_size):  # i행을 중간경로로
        for j in range(n_size):
            for k in range(n_size):
                if j != i and k != i:  # 중간노드 제외하고 체크
                    # j에서 i를 경유해 k로 가는 비용이 기존 비용보다 싸면 갱신
                    if mat[j][i] + mat[i][k] < mat[j][k]:
                        mat[j][k] = mat[j][i] + mat[i][k]

n_size, n_order = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n_size)]
floyd_warshall()
for i in range(n_order):
    st, ed, time = map(int, input().split())
    if mat[st-1][ed-1] <= time:  # 이내 = 이하
        print('Enjoy other party')
    else:
        print('Stay here')
