# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import Optional, List

"""
constraints:
  1 <= prices.length <= 3 * 10^4
  0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0]: 주식 보유하지 않은 상태에서의 최대 이익
        # dp[i][1]: 주식 보유한 상태에서의 최대 이익
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0  # 첫날 주식을 사지 않음
        dp[0][1] = -prices[0]  # 첫날 주식을 삼
        for i in range(1, n):
            # 주식 보유 X: 보유 X 유지 or 전날 보유 주식 판매
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 주식 보유 O: 전날 보유 O 유지 or 새 주식 구매
            # 최대 하나의 주식을 보유할 수 있으므로 중복 구매는 고려하지 않음
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n - 1][0]


inputdatas = [
    {"data": [[7, 1, 5, 3, 6, 4]], "answer": 7},
    {"data": [[1, 2, 3, 4, 5]], "answer": 4},
    {"data": [[7, 6, 4, 3, 1]], "answer": 0},
    {"data": [[1, 3, 2, 1, 4]], "answer": 5},
]

"""
LeetCode Medium.
제출 3.2M, 정답률 67.8%
그리디 풀이 후에 dp도 연습해봤다.
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
