# https://leetcode.com/problems/count-number-of-nice-subarrays/
from typing import Optional, List

"""
constraints:
"""


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        return 0


inputdatas = []

"""
LeetCode Hard.
제출 230.2K, 정답률 51.6%

"""
import inspect
functions = [
    value for value in Solution.__dict__.values() if inspect.isfunction(value)
]
my_func = functions[0][1]
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
