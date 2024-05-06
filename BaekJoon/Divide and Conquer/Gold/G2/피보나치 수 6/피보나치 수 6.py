# https://www.acmicpc.net/problem/11444
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n번째 피보나치 수를 1e9 + 7로 나눈 나머지를 출력하라.
"""


class Matrix:
    def __init__(self, ir, ic, identity=False, custom: list[list[int]] or None = None):
        self.r = ir
        self.c = ic
        if identity:  # 단위행렬
            self.mat = [[+(r == c) for c in range(self.c)] for r in range(self.r)]
        elif custom:
            self.mat = [[c for c in row] for row in custom]
        else:  # 영행렬
            self.mat = [[0] * self.c for _ in range(self.r)]

    # 행 반환. 행만 반환하면 열은 수정할 수 있음.
    def __getitem__(self, idx):
        return self.mat[idx]

    # 행 자체를 수정하는건 setitem으로.
    def __setitem__(self, key, value):
        self.mat[key] = value


def mat_mul(A: Matrix, B: Matrix) -> Matrix:
    C = Matrix(A.r, B.c)
    for i in range(A.r):
        for j in range(B.c):
            # 내적
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(A.c))
            C[i][j] %= MOD
    return C


def mat_pow(A: Matrix, ex: int) -> Matrix:
    if ex == 1:  # 1승이면
        return A
    if ex % 2 == 1:  # 홀수승이면
        return mat_mul(A, mat_pow(A, ex - 1))
    half = mat_pow(A, ex // 2)  # 짝수승이면
    return mat_mul(half, half)


def fib(n: int) -> int:
    if n in d:
        return d[n]
    tmpT = mat_pow(T, n - 1)
    d[n] = mat_mul(tmpT, V)[0][0]
    return d[n]


n = int(input())
MOD = int(1e9 + 7)
d = {0: 0, 1: 1}
T = Matrix(2, 2, custom=[[1, 1], [1, 0]])
V = Matrix(2, 1, custom=[[1], [0]])
print(fib(n))

"""
현 시점 골드2. 제출 22421. 정답률 47.742%
|F(n+1)| = |1 1|^n |F(1)|
| F(n) |   |1 0|   |F(0)|
선대 피보나치 행렬 이용하는 문제.
다른 사람들은 그냥 피보나치 규칙 찾아서 풀었는데
분할 정복을 이용한 거듭제곱 문제라서 행렬로 풀어봤다.
"""
