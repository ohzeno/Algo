# https://www.acmicpc.net/problem/13328
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
사업주 김모씨는 직원이 d번 이상 다른 직원에게 전화를 걸 수 없도록 시스템을 개편할 계획이다. 
이를 위해 다음 제약 조건에 따라 메시지 전달을 시작한 후 시간 t에서 
이루어진 전화 통화 수를 알고 싶다.

1. 각 호출에는 두 명의 직원만 포함됩니다.
2. 각 호출에는 하나의 시간 단위가 필요합니다.
3. 직원은 단위 시간당 하나의 통화에만 참여할 수 있습니다.
4. 각 직원은 정보를 받은 직후 연속 d 시간 동안 정보가 없는 직원에게 전화를 겁니다.
    김씨는 메시지 전달이 시작될 때만 직원에게 전화를 건다. 
    예를 들어, d=2인 경우는 다음 표와 같습니다.

시간 t	전화 통화	                                시간 t에서의 호출 수
0	    김씨는 A에게 전화를 걸어 메시지 전달을 시작한다.	1
1	    A는 B에게 전화를 겁니다(메시지를 전달하기 위해).	1
2	    A는 C에게 전화를 겁니다. B는 D에게 전화를 겁니다.	2
3	    B, C, D는 각각 E, F, G를 호출합니다.	        3

이 예에서 Kim은 시간 0에 A를 호출하여 메시지 전달을 시작합니다. 
호출에는 한 단위의 시간이 걸립니다. 
시간 1에서 A는 메시지를 가지고 있는 유일한 직원이고 정보가 없는 직원 B에게 전화를 겁니다. 
시간 2에서 A와 B 모두 메시지를 가지고 있습니다. 
A와 B는 정보가 없는 직원 C와 D에게 각각 전화를 겁니다. 
이 경우 각 직원은 다른 직원에게 두 번 이상 전화를 걸 수 없습니다.
위의 표와 같이 시간 3에 3번의 전화 통화가 이루어집니다.

d와 t가 주어지면 Kim이 메시지 전달을 시작한 후 시간 t에서의 호출 수를 출력하라.
"""
def mul(A, B):
    lc = len(B[0])
    C = [[0] * lc for _ in range(d+1)]
    for i in range(d+1):
        Ar = A[i]
        for j in range(lc):
            c = 0
            for k in range(d+1):
                c += Ar[k] * B[k][j]
            C[i][j] = c % 31991
    return C

def pow(A, e):
    if e == 1:
        return A
    elif e % 2:
        return mul(A, pow(A, e-1))
    hf = pow(A, e//2)
    return mul(hf, hf)

def init_V():
    vars = [0] * (d+1)
    vars[0:2] = [1,1]
    for i in range(2, d+1):  # i=2부터 d개 채울 때까지는 2배씩 늘어남.
        vars[i] = 2 * vars[i-1]
    return [[x] for x in vars]

def trans():
    mat = [[0] * (d+1) for _ in range(d+1)]
    for i in range(d):
        mat[i][i+1] = 1  # 다음 변수 당겨옴
    for j in range(1, d+1):  # 자신 앞쪽 총 d개 변수를 다 더함.
        mat[d][j] = 1
    return mat

d, t = map(int, input().split())
V = init_V()
if t < d+1:  # t가 d+1보다 작으면 변환 불필요.
    print(V[t][0])
    exit()
T = pow(trans(), t)
print(mul(T, V)[0][0])


"""
현 시점 플래 5. 제출 841. 정답률 41.444%
맞힌 사람 파이썬 그룹 1위, 숏코딩 모든 언어 1위

어떻게 변환행렬을 만들지가 관건이었다.
규칙성을 찾으려고 한참 고민했고, 처음에는 1차원 dp테이블 풀이를 만들었다.
d에 따라 dp[i]는 dp[i-1] + dp[i-2] + ... + dp[i-d]로 구할 수 있다.
즉, 자신 앞 d개 값을 다 더하면 된다.

이후 2차원 변환행렬을 이용해 해당 풀이를 적용하기 위해서 규칙에 맞는 변환행렬을 만들었다.
분할정복을 이용한 거듭제곱이기에 변환행렬을 t제곱 하고 dp테이블을 곱해서 답을 구했다.

몇 차례 시간초과에 당했는데 알고보니 문제 설명에는 없지만 
출력 설명에 m mod 31991을 출력하라고 되어있었다.
C[i][j] %= 31991를 추가하니 바로 통과했다.
"""