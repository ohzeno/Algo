# https://www.acmicpc.net/problem/14289
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
숭실 대학교 정보 과학관은 유배를 당해서 캠퍼스의 길 건너편에 있다. 
그래서 컴퓨터 학부 학생들은 캠퍼스를 ‘본대’ 라고 부르고 정보 과학관을 ‘정보대’ 라고 부른다. 
준영이 또한 컴퓨터 학부 소속 학생이라서 정보 과학관에 박혀있으며 항상 꽃이 활짝 핀 본대를 선망한다.
어느 날 준영이는 본대를 산책하기로 결심하였다.
숭실대학교 캠퍼스에는 n개의 건물이 있고, 인접한 두 건물을 잇는 도로 m개가 있다.
한 건물에서 바로 인접한 다른 건물로 이동 하는 데 1분이 걸린다. 
준영이는 산책 도중에 한번도 길이나 건물에 멈춰서 머무르지 않는다. 
준영이는 할 일이 많아서 딱 D분만 산책을 할 것이다. 
산책을 시작한 지 D분일 때, 정보 과학관에 도착해야 한다. 
이때 가능한 경로의 경우의 수를 구해주자.

첫째 줄에는 건물의 수 n개,도로의 수 m개가 주어진다.(1 ≤ n ≤ 50, 0 ≤ m ≤ 1000)
다음 m줄에는 두 건물를 잇는 간선 a, b가 주어진다.(1 ≤ a, b ≤ n, a ≠ b) 
특정 두 건물를 잇는 간선이 여러 번 나오지 않는다.
다음 줄에는 산책할 시간인 D분이 주어진다. 
1번 정점이 정보대이며, 준영이는 0분에 정보대에 위치할 것이다.(1 ≤ D ≤ 1,000,000,000)
"""
def mat_mul(A, B):
    return [
        [sum(a*b for a, b in zip(A_row, B_col)) % 1_000_000_007
         for B_col in zip(*B)]  # 행마다 열 순회
        for A_row in A  # 행 순회
    ]

def mat_pow(A, e):
    if e == 1:  # 1승이면
        return A
    if e % 2 == 1:  # 홀수승이면
        return mat_mul(A, mat_pow(A, e - 1))
    half = mat_pow(A, e // 2)  # 짝수승이면
    return mat_mul(half, half)

n, m = map(int, input().split())
mat = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    mat[a-1][b-1] = mat[b-1][a-1] = 1
print(mat_pow(mat, int(input()))[0][0])


"""
현 시점 골드 1. 제출 788. 정답률 68.731%
본대 산책1의 풀이에서 그래프 작성만 바꿔줬다.
"""