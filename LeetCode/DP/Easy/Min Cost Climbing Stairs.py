# https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan&id=level-1
from typing import Optional, List
"""
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        leng = len(cost)
        dp = [0] * leng
        dp[0], dp[1] = cost[0], cost[1]  # cost.length >= 2이므로
        for i in range(2, leng):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]  # 한 스텝, 두 스텝 중 작은 값과 현재 코스트 더함.
        return min(dp[-1], dp[-2])  # 마지막 두 스텝 중 작은 값 리턴.

inputdatas = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
]

"""
LeetCode Easy.
전형적인 dp문제.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
