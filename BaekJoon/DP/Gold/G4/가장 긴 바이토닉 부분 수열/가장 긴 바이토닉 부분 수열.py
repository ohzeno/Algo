# https://www.acmicpc.net/problem/11054
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
수열 S가 어떤 수 Sk를 기준으로 
S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 
그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 
은 바이토닉 수열이지만,  
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 
은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 
가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

첫째 줄에 수열 A의 크기 N이 주어지고, 1 ≤ N ≤ 1,000
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. 1 ≤ Ai ≤ 1,000
"""
n = int(input())
arr = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
for rr in range(1, n):
    for ll in range(rr):
        if arr[ll] < arr[rr]:  # 오름차순
            dp[rr][0] = max(dp[rr][0], dp[ll][0] + 1)
for ll in range(n-1, -1, -1):
    for rr in range(n-1, ll, -1):
        if arr[ll] > arr[rr]:  # 내림차순
            dp[ll][1] = max(dp[ll][1], dp[rr][1] + 1)
length = [sum(dp[i]) - 1 for i in range(n)]
print(max(length))


"""
현 시점 골드 4. 제출 55183. 정답률 50.994 %
생각난대로 풀었더니 통과했다. 골드라기엔 쉬운 문제.
"""