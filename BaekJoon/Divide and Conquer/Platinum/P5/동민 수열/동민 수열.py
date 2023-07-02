# https://www.acmicpc.net/problem/1529
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
동민 수열은 길이가 L이고, A[0], A[1], ..., A[L-1]와 같이 생긴 수열이다. 
또, 다음과 같은 성질을 가진다.

A[i]는 금민수이다. (0 ≤ i < L)
모든 i에 대해서 A[i] = Numbers[j]인 j가 적어도 하나 존재한다. (0 ≤ i < L)
모든 i에 대해서 A[i]의 마지막 자리는 A[i+1]의 첫 번째 자리와 같다. (0 ≤ i < L-1)
Numbers배열과 L이 주어졌을 때, 서로 다른 동민 수열의 개수를 
1,234,567,891로 나눈 나머지를 출력하는 프로그램을 작성하시오.

첫째 줄에 Numbers 배열의 크기 N과 L이 주어진다. 
1 <= N <= 50, 1 <= L <= 1,000,000,000
둘째 줄에 Numbers배열에 들어있는 수가 주어진다.
1<= 각각의 수 <= 1,000,000,000
"""
def mul(A, B):
    l = len(B[0])
    C = [[0]*2 for _ in range(2)]
    for r in range(2):
        Cr, Ar = C[r], A[r]
        for c in range(l):
            for k in range(2):
                Cr[c] += Ar[k] * B[k][c]
            Cr[c] %= m
    return C

def pow(A, e):
    if e == 1:
        return A
    if e % 2:
        return mul(A, pow(A, e-1))
    h = pow(A, e//2)
    return mul(h, h)

def mat():
    """
    T[0], T[1]은 각각 4, 7로 끝나는 수
    1, 2열은 각각 4, 7로 시작하는 수
    V[0], V[1]은 각각 4, 7로 끝나는 경우의 수
    TxV하면 V[0]은 e4*44 + e7*74, V[1]은 e4*47 + e7*77
    V의 각 원소에 뒷부분을 이어서 경우의 수를 갱신할 수 있다.
    """
    T = [[0] * 2 for _ in range(2)]
    for n in nums:
        nt = n[0] + n[-1]
        if nt == '44':
            T[0][0] += 1
        elif nt == '47':
            T[1][0] += 1
        elif nt == '74':
            T[0][1] += 1
        else:  # 77
            T[1][1] += 1
    return T, [[T[0][0]+T[0][1]],[T[1][0]+T[1][1]]]

n, l = map(int, input().split())
# 4, 7로만 이루어진 것만 필터링하고 중복제거.
nums = set(filter(lambda x: x.count('4') + x.count('7') == len(x), input().split()))
if l == 1:  # 원소 하나로만 만들 수 있으니 원소 갯수가 정답
    print(len(nums))
    exit()
m = 1234567891
T, V = mat()
V = mul(pow(T, l-1), V)
print((V[0][0] + V[1][0]) % m)  # 4, 7로 끝나는 경우의 수를 더한다.

"""
현 시점 플래 5. 제출 268. 정답률 27.556%
변환행렬을 어떻게 만들고, 변수 행렬을 어떻게 만들지 고민하는 데에 시간이 걸린다.
DP를 생각해서 길이에 대응하게 만들면 좀 편해진다.
"""