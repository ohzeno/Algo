# https://www.acmicpc.net/problem/13976
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
3xn 타일을 1x2, 2x1 블럭으로 채우는 방법의 수를 반환하라.
"""
class Matrix:
    def __init__(self, ir, ic, var=False):
        self.r = ir
        self.c = ic
        if var:  # 변수행렬
            self.mat = [[0] * self.c]
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
            C[i][j] %= 1_000_000_007
    return C

def mat_pow(A: Matrix, ex: int) -> Matrix:
    if ex == 1:  # 1승이면
        return A
    elif ex % 2 == 1:  # 홀수승이면
        return mat_mul(A, mat_pow(A, ex - 1))
    half = mat_pow(A, ex // 2)  # 짝수승이면
    return mat_mul(half, half)

def sol(n: int) -> int:
    if n % 2:
        return 0
    elif n == 2:
        return 3
    var = Matrix(1, 2, var=True)  # 변수행렬
    var[0] = [1, 3]
    trans = Matrix(2, 2)  # 변환행렬
    trans[0] = [0, -1]
    trans[1] = [1, 4]
    res = mat_mul(var, mat_pow(trans, n//2-1))  # 변환결과
    return res[0][1]
print(sol(int(input())))

"""
현 시점 플래 5. 제출 1703. 정답률 46.725%
변환행렬 만들어서 분할정복 거듭제곱 하면 된다.
정답률 높은 이유가 있음.
"""