# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        cnt = 0
        return cnt

inputdatas = [

]

"""
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for nums, k in inputdatas:
    print(functions[0][1](nums, k))
