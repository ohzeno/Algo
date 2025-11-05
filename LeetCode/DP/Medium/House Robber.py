# https://leetcode.com/problems/house-robber/
from typing import Optional, List

"""
constraints:
  • 1 <= nums.length <= 100
  • 0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


inputdatas = [
    {"data": [[1, 2, 3, 1]], "answer": 4},
    {"data": [[2, 7, 9, 3, 1]], "answer": 12}
]

"""
LeetCode Medium.
제출 6M, 정답률 52.6%
간단한 dp문제. dp[1]을 미리 지정해주면 더 직관적
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
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
