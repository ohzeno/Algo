# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
from typing import Optional, List

"""
constraints:
  1 <= prices.length <= 10^5
  0 <= prices[i] <= 10^5
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_prices = len(prices)
        # dp[i][j][k]
        # i: 날짜, j: 수행중인 트랜잭션 횟수, k: 주식 보유 여부
        # 동시에 두 트랜잭션에 들어갈 수 없으므로 j는 commit이 아니라 수행중인 트랜잭션 횟수.
        # 즉, j는 구매할 때만 늘어난다.
        dp = [[[0] * 2 for _ in range(3)] for _ in range(l_prices)]
        dp[0][1][1] = -prices[0]
        dp[0][1][0] = dp[0][2][0] = dp[0][2][1] = float('-inf')
        for i in range(1, l_prices):
            for j in range(1, 3):
                # 전날 주식 보유X 유지, 전날 보유 주식 판매
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # 전날 보유 주식 유지, 전날 주식 보유 X + 오늘 주식 구매
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        # i를 0까지 포함하는 이유는, 주식을 사고판 것이 오히려 마이너스일 수 있기 때문.
        return max(dp[-1][i][0] for i in range(3))


inputdatas = [
    {"data": [[3, 3, 5, 0, 0, 3, 1, 4]], "answer": 6},
    {"data": [[1, 2, 3, 4, 5]], "answer": 4},
    {"data": [[7, 6, 4, 3, 1]], "answer": 0}
]

"""
LeetCode Hard.
제출 1.4M, 정답률 49.3%
이건 오히려 dp가 이해하기 편한듯.
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
