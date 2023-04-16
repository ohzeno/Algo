# https://www.acmicpc.net/problem/12738
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 10 20 30 50 이고, 길이는 4이다.
"""
from bisect import bisect_left as bl
n = int(input())
datas = list(map(int, input().split()))
lis = [datas.pop(0)]
leng = 1
for data in datas:
    if lis[-1] < data:
        lis.append(data)
        leng += 1
    else:
        ll = bl(lis, data)
        lis[ll] = min(lis[ll], data)
print(leng)

"""
현 시점 골드2. 제출 11278, 정답률 62.023%
가장 긴 증가하는 부분 수열 2와 비교해서 Ai가 음수로 확장되고 상/하한이 커졌다.
이분탐색 자체는 음, 양과 상관없기에 이전과 같은 코드로 통과.
"""
