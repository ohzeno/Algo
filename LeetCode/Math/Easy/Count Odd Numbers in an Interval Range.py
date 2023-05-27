# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
from typing import Optional, List
"""
0 <= low <= high <= 10^9
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low % 2 and not high % 2:  # ee인 경우만
            return (high - low) // 2
        return (high - low) // 2 + 1

inputdatas = [
    [3, 7],
    [8, 10],
]

"""
LeetCode Easy
처음엔 리스트에 for문으로 low~high까지 홀수만 넣고 len을 반환했으나 시간초과가 발생했다.
케이스를 나눠보니 oo, oe, eo는 (h-l)//2 + 1, ee는 (h-l)//2가 홀수의 갯수였다. 
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
