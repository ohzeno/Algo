# https://leetcode.com/problems/product-of-array-except-self/
from typing import Optional, List

"""
constraints:
  • 2 <= nums.length <= 10^5
  • -30 <= nums[i] <= 30
  • The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""
from operator import mul
from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre = list(accumulate(nums, lambda x, y: x * y))
        pre = list(accumulate(nums, mul))
        suf = list(accumulate(nums[::-1], mul))[::-1]
        if nums.count(0) > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            pre_part = pre[i - 1] if i != 0 else 1
            suf_part = suf[i + 1] if i != len(nums) - 1 else 1
            nums[i] = pre_part * suf_part
        return nums


inputdatas = [
    {"data": [[1, 2, 3, 4]], "answer": [24, 12, 8, 6]},
    {"data": [[-1, 1, 0, -3, 3]], "answer": [0, 0, 9, 0, 0]},
    {"data": [[0, 0]], "answer": [0, 0]},
    {"data": [[2, 3, 0, 0]], "answer": [0, 0, 0, 0]},
    {"data": [[0, 2, 3, 4]], "answer": [24, 0, 0, 0]},
]

"""
LeetCode Medium.
제출 5.2M, 정답률 67.5%
무식하게 풀고 풀이들 보니 prefix, suffix product를 이용한 풀이가 많았다.
파이썬에 reduce 있는 것도 처음 알았고 mul도 처음 알았다.
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
