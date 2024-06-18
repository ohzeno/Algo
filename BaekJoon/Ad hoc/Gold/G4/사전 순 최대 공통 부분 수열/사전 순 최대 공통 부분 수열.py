# https://www.acmicpc.net/problem/30805
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
어떤 수열이 다른 수열의 부분 수열이라는 것은 다음을 의미합니다.
    해당 수열의 원소들이 다른 수열 내에서 순서대로 등장합니다.
    예를 들어, {1,1,5}는 {3, 1 ,4, 1 , 5 ,9}의 부분 수열이지만, {1,5,1}의 부분 수열은 아닙니다.
또한, 어떤 수열이 다른 수열보다 사전 순으로 나중이라는 것은 다음을 의미합니다.
    두 수열 중 첫 번째 수가 큰 쪽은 사전 순으로 나중입니다.
    두 수열의 첫 번째 수가 같다면, 첫 번째 수를 빼고 두 수열을 다시 비교했을 때 사전 순으로 나중인 쪽이 사전 순으로 나중입니다.
    길이가 0인 수열과 다른 수열을 비교하면, 다른 수열이 사전 순으로 나중입니다.
양의 정수로 이루어진 길이가 N인 수열 {A_1,...,A_N}이 주어집니다. 
마찬가지로 양의 정수로 이루어진 길이가 M인 수열 {B_1,...,B_M}이 주어집니다.
수열 A와 수열B가 공통으로 갖는 부분 수열들 중 사전 순으로 가장 나중인 것을 구하세요.

첫 줄에 수열 A의 길이 N이 주어집니다. (1 <= N <= 100)
둘째 줄에 N개의 양의 정수 A_1,A_2,...,A_N이 주어집니다. (1 <= A_i <= 100)
셋째 줄에 수열 B의 길이 M이 주어집니다. (1 <= M <= 100)
넷째 줄에 M개의 양의 정수 B_1,B_2,...,B_M이 주어집니다. (1 <= B_i <= 100)

A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 K를 출력하세요.
K != 0이라면, 다음 줄에 K개의 수를 공백으로 구분해 출력하세요. 
i번째 수는 A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 i번째 수입니다.
"""


def find(pA, pB):
    a_st_n = 0
    b_d = {}
    for i in range(pB, m):
        b_d.setdefault(B[i], []).append(i)
    for i in range(pA, n):
        a = A[i]
        if a <= a_st_n or a not in b_d:
            continue
        a_st_i, a_st_n = i, a
        b_st_i = min(b_d[a])
    return [a_st_n] + find(a_st_i + 1, b_st_i + 1) if a_st_n else []


n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))
res = find(0, 0)
k = len(res)
print(k)
print(*res)


"""
현 시점 골드 4. 제출 1264. 정답률 31.417 %
최대 공통 부분 수열이 제목이라 처음엔 lcs를 찾았는데
그냥 공통 부분 수열 중 사전순 가장 나중을 찾는 문제라 '최대'와 전혀 관련 없다.
문제 제목이 낚시...
"""
