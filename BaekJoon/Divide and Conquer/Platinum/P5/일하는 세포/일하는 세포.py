# https://www.acmicpc.net/problem/17401
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n개의 거점이 있고 일부는 서로 이어져있다.
거점 사이 통로 통과에 1초가 걸린다.
매 초 거점 사이 연결관계가 바뀐다.
매 초 무조건 통로를 하나 타야 한다.
일부 통로는 출발과 도착 거점이 같을 수도 있다.
일부 거점은 특정 순간 나가는 통로가 없을 수 있는데,
이 때는 도착한 지 1초 후에 파괴된다.
몸 속 혈관 지도가 T초 주기로 반복된다.
거점 A에서 D초후 B에 도달하게 되는 경우의 수를 
모든 거점의 순서쌍에 대해 구하고자 한다.
한 경로는 D초동안 통과한 통로의 순열로 정의된다.
D초동안 한 거점에서 다른 거점까지 움직일 수 있는 경우의 수를 구하라.

첫 줄에 주기T, 거점 개수 N, 움직이는 시간 D가 주어진다.
1 <= T <= 100, 2 <= N <= 20, 0 <= D <= 10^9
이후 T줄동안 1번부터 T번까지 혈관 지도가 주어진다.
    첫 줄에 통로 갯수 Mi가 주어진다 0<= Mi <= N^2
    이후 Mi줄동안 a,b,c가 공백으로 구분되어 주어진다.
        거점a에서 거점b로 가는 서로 다른 단방향 통로가 c개 있음을 의미
        1 <= a,b <= N, 1 <= c <= 10^3
    매 혈관 지도에 중복된 연결 관계는 주어지지 않음
i초에서 i+1초동안 이동할 때는 (i%T+1) 혈관 지도가 적용된다.
출력은 N개 줄로 구성되며, i번째 줄에 N개의 정수 xij를 공백으로 구분하여 출력한다.
xij는 0초 때 거점i에서 출발하여 정확히 D초에 거점 j에 위치하게 되는 
경로의 수를 1_000_000_007로 나눈 나머지다.
"""
def mul(A, B):
    # return [
    #     [sum(a*b for a, b in zip(A_row, B_col)) % 1_000_000_007
    #      for B_col in zip(*B)]  # 행마다 열 순회
    #     for A_row in A  # 행 순회
    # ]
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 내적
            # C[i][j] = sum(A[i][k] * B[k][j] for k in range(N))
            # C[i][j] %= 1_000_000_007
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= 1_000_000_007
    return C

def pow(A, e):
    if e == 1:  # 1승이면
        return A
    elif e%2 == 1:  # 홀수승이면
        return mul(A, pow(A, e-1))
    hf = pow(A, e//2)  # 짝수승이면
    return mul(hf, hf)

T, N, D = map(int, input().split())
if not D:  # 0초면 경우의 수 0
    for _ in range(N):
        print(*[0]*N)
    exit()
maps = [[[0]*N for _ in range(N)] for _ in range(T)]
for n in range(T):
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        maps[n][a-1][b-1] = c
quo, rem = divmod(D, T)
res = [[1 if i == j else 0 for i in range(N)] for j in range(N)]  # 단위행렬
if quo:  # 1주기 이상
    for i in range(T):  # T개 지도 순서대로 지나는 행렬
        res = mul(res, maps[i])
    res = pow(res, quo)  # 거듭제곱
for i in range(rem):  # 나머지 지도 순서대로 지나는 행렬
    res = mul(res, maps[i])
for r in res:
    print(*r)

"""
현 시점 플래 5. 제출 937. 정답률 49.938%
역시나 행렬 거듭제곱으로 풀었다.
그래프 경로의 수를 행렬로 어떻게 풀어야 할 지 몰라서 본대 산책을 몇 풀어본 후 풀었다.
경우의 수를 행렬로 푸는 방법을 안다면 그렇게 어렵지 않은 문제.
예외처리만 잘해주면 된다.

다른 사람들 풀이를 살펴보니 상당수는 내 풀이랑 비슷한 논리다.
"""