# https://leetcode.com/problems/climbing-stairs/
from typing import Optional, List
"""
1 <= n <= 45
"""
from functools import cache
class Solution:
    @cache
    def dp(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.dp(n - 1) + self.dp(n - 2)

    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 올라가는 방법의 수
        # dp[0] = dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        return self.dp(n)

inputdatas = [
    2, 3
]

"""
LeetCode Easy
dp치고는 쉬운 문제.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
