# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import Optional, List

"""
constraints:
  • 1 <= nums1.length, nums2.length <= 1000
  • 0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


inputdatas = [
    {"data": [[1, 2, 2, 1], [2, 2]], "answer": [2]},
    {"data": [[4, 9, 5], [9, 4, 9, 8, 4]], "answer": [9, 4]}
]

"""
LeetCode Easy.
제출 2.2M, 정답률 77.0%

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
