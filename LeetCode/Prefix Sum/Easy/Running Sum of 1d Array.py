# https://leetcode.com/problems/running-sum-of-1d-array/
"""
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i]
        return dp

inputdatas = [
    [1,2,3,4],
    [1,1,1,1,1],
    [3,1,2,10,1]
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Easy.
전형적인 누적합 문제. 2분도 안걸렸다.
"""
