# https://leetcode.com/problems/add-two-integers/
from typing import Optional, List
"""
-100 <= num1, num2 <= 100
"""
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

inputdatas = [
    [12, 5],
    [-10, 4],
]

"""
LeetCode Easy
단순한 덧셈.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
