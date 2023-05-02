# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
from typing import Optional, List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        return cnt

inputdatas = [

]

"""
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
