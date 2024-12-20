# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
from typing import Optional, List

"""
constraints:
  1 <= k <= 100
  1 <= prices.length <= 1000
  0 <= prices[i] <= 1000
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp[a][b][c]
        # a: 날짜, b: 수행중인 트랜잭션 횟수, c: 주식 보유 여부
        # 동시에 두 트랜잭션에 들어갈 수 없으므로 b는 commit이 아니라 수행중인 트랜잭션 횟수.
        # 즉, b는 구매할 때만 늘어난다.
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        dp[0][1][1] = -prices[0]
        for b in range(1, k+1):
            # 첫날에 트랜잭션 완료했을 수가 없음
            dp[0][b][0] = float('-inf')
            if b > 1:  # 첫날에 두 번째 이상의 트랜잭션을 완료하고 주식을 보유할 수 없음
                dp[0][b][1] = float('-inf')
        for t in range(1, n):
            for d in range(1, k+1):
                # 전날 주식 보유X 유지, 전날 보유 주식 판매
                dp[t][d][0] = max(dp[t-1][d][0], dp[t-1][d][1] + prices[t])
                # 전날 보유 주식 유지, 전날 주식 보유 X + 오늘 주식 구매
                dp[t][d][1] = max(dp[t-1][d][1], dp[t-1][d-1][0] - prices[t])
        # i를 0까지 포함하는 이유는, 주식을 사고판 것이 오히려 마이너스일 수 있기 때문.
        return max(dp[-1][i][0] for i in range(k+1))


inputdatas = [
    {"data": [2, [2, 4, 1]], "answer": 2},
    {"data": [2, [3, 2, 6, 5, 0, 3]], "answer": 7}
]

"""
LeetCode Hard.
제출 1.1M, 정답률 44.7%
3과 같은 로직으로 풀었다.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
