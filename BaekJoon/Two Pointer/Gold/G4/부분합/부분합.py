# https://www.acmicpc.net/problem/1806
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
10 <= N <= 100,000
1 <= S <= 100,000,000
"""
n, s = map(int, input().split())
datas = list(map(int, input().split()))
for i in range(1, n):
    datas[i] += datas[i-1]
if datas[-1] < s:
    print(0)
    exit()
ll = rr = 0
min_len = n
while rr < n:
    cur_sum = datas[rr] - (datas[ll-1] if ll else 0)
    if cur_sum < s:
        rr += 1
    else:
        min_len = min(min_len, rr - ll + 1)
        ll += 1
print(min_len)


"""
현 시점 골드 4. 제출 85241. 정답률 25.713 %
부분합 문제.
"""