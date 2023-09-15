# https://leetcode.com/problems/count-number-of-nice-subarrays/
from typing import Optional, List
"""
constraints:
"""
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        return 0

inputdatas = [

]

"""
LeetCode Hard.
제출 230.2K, 정답률 51.6%

"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(*t))
