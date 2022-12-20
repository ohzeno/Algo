# https://www.acmicpc.net/problem/2075
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    mat = list(map(int, input().split()))
    if _ == 0:
        rank = mat  # 첫 n개 원소
    else:
        min_num = min(rank)  # rank에 들어간 원소 중 최소값
        for i in range(n):
            if mat[i] > min_num:  # 새 데이터가 현재 rank의 n번째 큰 원소보다 크면 삽입
                rank.append(mat[i])
    rank = sorted(rank)[-n:]  # 메모리 초과 해결 위해 큰 순으로 n개로 초기화
print(rank[0])  # 오름차순이므로 0이 n번째 큰 원소
