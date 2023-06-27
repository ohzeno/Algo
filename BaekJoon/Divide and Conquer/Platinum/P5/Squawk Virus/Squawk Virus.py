# https://www.acmicpc.net/problem/11767
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
바이러스를 받은 노드는 1분 후 모든 이웃 노드에 스쿼크를 보낸다.
그래프와 초기 감염 사이트가 주어지면 
특정 시간 t에 얼마나 많은 스쿼크가 만들어지는지 구하라.
유저 수 1 ≤ n ≤ 100
길 0 ≤ m ≤ n(n − 1)/2
초기 감염 유저 s < n
시간 t < 10
연결은 양방향. 중복 연결은 주어지지 않는다.
"""
def mul(A, B):
    l = len(B[0])
    C = [[0]*l for _ in range(n)]
    for r in range(n):
        Cr, Ar = C[r], A[r]
        for c in range(l):
            # Cr[c] = sum(Ar[k] * B[k][c] for k in range(n))
            for k in range(n):
                Cr[c] += Ar[k] * B[k][c]
    return C
    # return [[sum(a*b for a,b in zip(R,C)) for C in zip(*B)]for R in A]

def pow(A, e):
    if e == 1:
        return A
    elif e % 2:
        return mul(A, pow(A, e-1))
    h = pow(A, e//2)
    return mul(h, h)

n, m, s, t = map(int, input().split())
graph = [[0] * n for _ in range(n)]
v = [[0] for _ in range(n)]
v[s][0] = 1
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
v = mul(pow(graph, t), v)
print(sum(v[i][0] for i in range(n)))

"""
현 시점 플래 5. 제출 79. 정답률 49.254%
연결그래프 자체가 변환행렬이라 편한 문제.
저번주에 봤을 때는 플래 4였는데 그 사이 내려왔다.

맞힌 사람 python 그룹 1위, 숏코딩 모든 언어 1위.

코드를 수정해보면서 제출했는데, 
이 문제는 같은 코드도 제출마다 시간 차이가 너무 커서
제출 결과로는 코드와 시간복잡도의 관계를 추정할 수가 없었다.
"""