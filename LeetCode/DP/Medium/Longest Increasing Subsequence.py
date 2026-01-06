# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import Optional, List

"""
constraints:
  • 1 <= nums.length <= 2500
  • -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i]는 nums[i]를 마지막 원소로 하는 가장 긴 증가하는 부분 수열의 길이
        for b in range(1, n):
            for a in range(b):
                if nums[a] < nums[b]:
                    dp[b] = max(dp[b], dp[a] + 1)
        return max(dp)


inputdatas = [
    {"data": [[10, 9, 2, 5, 3, 7, 101, 18]], "answer": 4},
    {"data": [[0, 1, 0, 3, 2, 3]], "answer": 4},
    {"data": [[7, 7, 7, 7, 7, 7, 7]], "answer": 1}
]

"""
LeetCode Medium.
제출 4.2M, 정답률 58.8%

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
