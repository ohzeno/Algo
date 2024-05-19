# https://www.acmicpc.net/problem/2143
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
한 배열 A[1],...,A[n]에 대해, 
부 배열은 A[i],...,A[j](1 ≤ i ≤ j ≤ n)을 말한다.
각 원소가 정수인 두 배열 A, B가 주어졌을 때, 
A의 부 배열 합에 B의 부 배열 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하라.
-10^9 ≤ T ≤ 10^9, 1 ≤ n, m ≤ 1,000, 0 ≤ |A[i]|, |B[i]| ≤ 10^6
"""
from itertools import accumulate as acc
from collections import defaultdict

def get_data():
    return int(input()), list(acc(map(int, input().split()), initial=0))

t = int(input())
len_a, a_acc = get_data()
len_b, b_acc = get_data()
a_d = defaultdict(int)
for i in range(len_a):
    for j in range(i+1, len_a+1):
        sub_sum = a_acc[j] - a_acc[i]
        a_d[sub_sum] += 1
res = 0
for i in range(len_b):
    for j in range(i+1, len_b+1):
        res += a_d[t - (b_acc[j] - b_acc[i])]
print(res)


"""
현 시점 골드 3. 제출 29037. 정답률 31.854 %
보자마자 든 생각이 Two Sum 방식으로 dict를 사용하면 되겠다는 것이었다.
다음으로, 그러려면 부분합을 구해서 카운팅 해둬야겠다고 생각했다.
부분합을 어떻게 구할까 했는데 누적합이 편했다.
"""