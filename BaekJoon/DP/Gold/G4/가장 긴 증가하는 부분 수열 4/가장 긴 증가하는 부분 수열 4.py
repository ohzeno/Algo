# https://www.acmicpc.net/problem/14002
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 10 20 30 50 이고, 길이는 4이다.
"""

n = int(input())
datas = list(map(int, input().split()))
dp = [[1, [datas[i]]] for i in range(n)]  # [길이, lis]
max_idx = 0
for rr in range(1, n):
    for ll in range(rr):
        # 우항이 좌항보다 크고, 좌항에 이었을 때 현재보다 더 길면
        if datas[ll] < datas[rr] and dp[ll][0] + 1 > dp[rr][0]:
            dp[rr][0] = dp[ll][0] + 1  # 길이 업데이트
            dp[rr][1] = dp[ll][1] + [datas[rr]]  # lis 업데이트
            if dp[rr][0] > dp[max_idx][0]:  # lis 인덱스 업데이트
                max_idx = rr
print(dp[max_idx][0])
print(*dp[max_idx][1])

"""
현 시점 골드4. 제출 31352, 정답률 39.238%
가장 긴 증가하는 부분 수열 1과 n, ai 범위가 같은 대신
lis 자체를 추가로 출력해야 한다.
이분탐색을 사용하는 방법으로는 최종 배열이 여러 is가 중첩된 배열이라 추가 작업이 필요하다.
n의 범위가 작으므로 1을 풀 때 처럼 2중 for문 dp를 사용하고, 
dp를 2차원으로 만들어 배열을 기록해줬다.
"""
