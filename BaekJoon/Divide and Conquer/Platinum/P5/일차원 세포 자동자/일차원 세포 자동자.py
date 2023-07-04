# https://www.acmicpc.net/problem/3827
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
세포는 0번부터 N-1번.
각 세포는 M보다 작은 음이 아닌 정수 상태를 갖고있다. 
세포의 상태는 시간이 1 지날 때마다 진화한다. 
시간 t에서 i번째 세포의 상태를 S(i,t)로 나타낸다. 
t+1일 때의 상태는 다음과 같은 방정식을 통해 구할 수 있다.

S(i,t+1) = (A × S(i-1,t) + B × S(i,t) + C × S(i+1,t)) % M

위 식에서 A, B, C는 음이 아닌 정수. i<0 또는 N ≤ i인 경우에 S(i,t) = 0이다.

일차원 세포 자동자의 초기 상태가 주어졌을 때, 
시간이 T만큼 지난 뒤, 세포의 상태를 구하는 프로그램을 작성하시오.

각 테스트 케이스는 다음과 같은 형식으로 이루어져 있다.
N M A B C T
S(0,0) S(1,0) ... S(N-1,0)

0 < N ≤ 50, 0 < M ≤ 1000, 0 ≤ A,B,C < M, 0 ≤ T ≤ 109
입력의 마지막 줄에는 0이 여섯 개 주어진다.

각 테스트 케이스에 대해서, 시간 T에서 세포의 상태를 출력한다. 
S(0,T) S(1,T) ... S(N-1,T)
각 세포의 상태는 정수이고, 공백으로 구분되어야 한다.
"""
# from functools import cache
# @cache
def make_trans():
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        row = mat[i]
        if i > 0:
            row[i-1] = a
        row[i] = b
        if i < n-1:
            row[i+1] = c
    return mat_pow(mat, t)

def mat_mul(A, B):
    C = [[0] * n for _ in range(n)]
    lb = len(B[0])
    for r in range(n):
        Cr, Ar = C[r], A[r]
        for c in range(lb):
            # C[r][c] = sum(A[r][k] * B[k][c] for k in range(n)) % m
            for k in range(n):
                Cr[c] += Ar[k] * B[k][c]
            Cr[c] %= m
    return C
    # return [[sum(a*b for a, b in zip(A_row, B_col)) % m for B_col in zip(*B)] for A_row in A]

def mat_pow(A, e):
    if e == 1:
        return A
    elif e % 2:
        return mat_mul(A, mat_pow(A, e-1))
    half = mat_pow(A, e//2)
    return mat_mul(half, half)

while True:
    n, m, a, b, c, t = map(int, input().split())
    if not n:
        break
    elif not t:
        print(*(input().split()))
        continue
    vars = [[v] for v in map(int, input().split())]
    trans = make_trans()
    vars = mat_mul(trans, vars)
    print(*[r[0] for r in vars])


"""
현 시점 플래 5. 제출 259. 정답률 43.529%
변환행렬 만드는 부분이 반복적으로 사용돼서 cache를 사용해봤는데 오히려 느려졌다.
644B 960ms에서 숏코딩 한다고 행렬곱에 list comprehension을 써봤는데 510B 6680ms이 돼버렸다.
어찌됐든 맞힌 사람 python 1위, 숏코딩 모든 언어 1위.
"""