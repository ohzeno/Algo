# https://www.acmicpc.net/problem/2738
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n)]
mat2 = [list(map(int, input().split())) for _ in range(n)]
# 각 행렬의 줄 매칭해서 원소끼리 더하기
mat3 = [list(map(lambda x, y: x + y, mat1[i], mat2[i])) for i in range(n)]
for j in range(n):
    print(*mat3[j])
