# https://www.acmicpc.net/problem/11053
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
"""
n = int(input())
datas = list(map(int, input().split()))
dp = [1] * n
for rr in range(n):
    for ll in range(rr):
        if datas[ll] < datas[rr]:
            dp[rr] = max(dp[rr], dp[ll] + 1)
print(max(dp))

"""
현 시점 실버2. 제출 131758, 정답률 37.441%
'증가하는 부분 수열'의 정의가 없다. 예시 하나만 있는데, 충분한 설명이 되지 않는다.
각 원소가, 자신보다 왼쪽에 있는 원소보다 크다는 조건이 필요하다.
'증가하는'이 그 뜻을 포함한다고 주장할 수 있지만
10 10 10 20 의 경우도 '증가하는'이 될 수 있다. 
'무엇'이 증가하는지에 대한 명확한 묘사가 없기에 중의적이라 이런 문제가 발생한다.
좋은 문제는 아니다.
일단 각 원소가 자신보다 왼쪽에 있는 원소보다 크다는 조건으로 생각해봤다.
제일 먼저 생각난건 2중 for문이었다.
n이 최대 1000인데 2중 for문에 max까지 써서 시간 제한 1초를 통과할 수 있을까 걱정됐는데
싱겁게 통과했다.
"""