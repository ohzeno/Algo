# https://leetcode.com/problems/product-of-array-except-self/
from typing import Optional, List

"""
constraints:
  • 2 <= nums.length <= 10^5
  • -30 <= nums[i] <= 30
  • The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # zero_cnt = 0
        # for n in nums:
        #     if n != 0:
        #         prod *= n
        #     else:
        #         zero_cnt += 1
        prod = reduce(lambda a, b: a * b if b != 0 else a, nums, 1)
        zero_cnt = nums.count(0)
        if zero_cnt > 1:
            return [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                nums[i] = prod if n == 0 else 0
            else:
                nums[i] = prod // n
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
파이썬에 reduce 있는 것도 처음 알았다.
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
