# https://www.acmicpc.net/problem/14003
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
lis = [datas[0]]
leng = 1
dp = [1] * n  # 해당 지점까지의 lis 길이
for idx, data in enumerate(datas[1:], 1):
    if lis[-1] < data:  # lis보다 크면 추가
        lis.append(data)
        leng += 1
        dp[idx] = leng  # lis 길이 업데이트
    else:  # lis보다 작거나 같을 경우
        t_idx = bl(lis, data)  # 중첩lis에서 이어붙일 수 있는 위치
        if lis[t_idx] > data:  # 기존보다 작으면 값 업데이트
            lis[t_idx] = data
        dp[idx] = t_idx + 1  # 이어붙일 길이에 +1.
ans = []
tmp_l = leng
for i in range(n - 1, -1, -1):  # 역순으로 탐색
    if dp[i] == tmp_l:  # 길이 역순으로 탐색하면 lis 완성.
        # lis[5]에서 왼쪽으로 가장 가까운 lis[4]가 길이 5에 이어진 값.
        # 왼쪽에서부터 탐색하며 더 크면 바로 lis에 추가했기에 가능한 방법.
        ans.append(datas[i])
        tmp_l -= 1
print(leng)
print(*ans[::-1])

"""
현 시점 플래티넘5. 제출 23719, 정답률 34.083%
가장 긴 증가하는 부분 수열 3에 lis를 추가로 출력하는 문제.
n이 커서 dp로 풀긴 힘들다. 이분탐색으로 풀면 lis 기록이 귀찮아진다.
처음에는 딕셔너리에 매번 기록해보며 한참 고생했는데
알고보니 lis테이블을 만들면서 기존 2중for문 dp처럼 dp테이블에 
해당 위치까지의 lis 길이만 기록하면 해결되는 문제였다.
lis 알고리즘 2개를 종합하면 해결되는 문제.
"""
