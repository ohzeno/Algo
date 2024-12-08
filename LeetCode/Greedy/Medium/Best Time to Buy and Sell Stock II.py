# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import Optional, List

"""
constraints:
  1 <= prices.length <= 3 * 10^4
  0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


inputdatas = [
    {"data": [[7, 1, 5, 3, 6, 4]], "answer": 7},
    {"data": [[1, 2, 3, 4, 5]], "answer": 4},
    {"data": [[7, 6, 4, 3, 1]], "answer": 0},
    {"data": [[1, 3, 2, 1, 4]], "answer": 5},
]

"""
LeetCode Medium.
제출 3.2M, 정답률 67.8%
dp연습하려고 했는데 이 그리디 로직도 고민할 만 했다.
하루어치 수익만 넣어도 연속 보유 수익은 반영된다.
중간에 떨어지면 어떡하나 싶었는데
2 3 1 4 식이면 2-4가 아니가 2-3, 1-4가 이득이라 상관없다.
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
