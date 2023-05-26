# https://leetcode.com/problems/find-pivot-index/
from typing import Optional, List
"""
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leng = len(nums)
        dp = [0] * leng  # dp[i] = sum(nums[:i + 1])
        dp[0] = nums[0]
        for i in range(1, leng):
            dp[i] = dp[i-1] + nums[i]
        for i in range(leng):
            if dp[i] - nums[i] == dp[-1] - dp[i]:  # 왼쪽 합 == 오른쪽 합
                return i
        return -1
        # total = sum(nums)
        # lsum = 0
        # for i, n in enumerate(nums):
        #     if lsum == total - lsum - n:
        #         return i
        #     lsum += n
        # return -1

inputdatas = [
    [1, 7, 3, 6, 5, 6],
    [1, 2, 3],
    [2, 1, -1]
]

"""
LeetCode Easy.
전형적인 Prefix Sum 문제.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
