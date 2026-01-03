# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
from typing import Optional, List

"""
constraints:
  • 0 <= num <= 10^15
"""


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]



inputdatas = [
    {"data": [33], "answer": [10, 11, 12]},
    {"data": [4], "answer": []}
]

"""
LeetCode Medium.
제출 96.4K, 정답률 65.2%

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
