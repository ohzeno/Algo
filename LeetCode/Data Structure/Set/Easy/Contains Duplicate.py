# https://leetcode.com/problems/contains-duplicate/
from typing import Optional, List
"""
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False

inputdatas = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]

"""
LeetCode Easy
중복검사. 제한이 빡빡하지 않아서 그냥 len을 썼다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
