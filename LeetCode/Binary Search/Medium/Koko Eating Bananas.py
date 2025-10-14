# https://leetcode.com/problems/koko-eating-bananas/
from typing import Optional, List

"""
constraints:
  • 1 <= piles.length <= 10^4
  • piles.length <= h <= 10^9
  • 1 <= piles[i] <= 10^9
"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ll, rr = 1, max(piles)
        succeeded = None
        while ll <= rr:
            mid = (ll + rr) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
            if hour <= h:
                succeeded = mid
                rr = mid - 1
            else:
                ll = mid + 1
        return succeeded


inputdatas = [
    {"data": [[3, 6, 7, 11], 8], "answer": 4},
    {"data": [[30, 11, 23, 4, 20], 5], "answer": 30},
    {"data": [[30, 11, 23, 4, 20], 6], "answer": 23}
]

"""
LeetCode Medium.
제출 2.7M, 정답률 49.2%
처음엔 몫, 나머지로 조건문 걸었는데 ceil이 편하다.
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
