# https://www.acmicpc.net/problem/10830
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
크기가 N*N인 행렬 A가 주어진다. 
이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
"""


def mat_mul(A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
            C[i][j] %= 1000
    return C


def mat_pow(A, ex):
    if ex == 1:
        return A
    if ex % 2:
        return mat_mul(A, mat_pow(A, ex - 1))
    half = mat_pow(A, ex // 2)
    return mat_mul(half, half)


n, b = map(int, input().split())
mat = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(n)]
ans = mat_pow(mat, b)
for row in ans:
    print(*row)


"""
현 시점 골드 4. 제출 39270. 정답률 34.632 %
클래스 만들어볼까 하다가 귀찮아서 넘겼다.
자주 하던 내용이라 대충했다가 80%에서 틀렸는데, 
원소가 1000이고 1승인 경우에도 원소를 1000으로 나눠야 했다.
"""
