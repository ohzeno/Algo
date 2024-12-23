# https://leetcode.com/problems/first-missing-positive/
from typing import Optional, List

"""
constraints:
  1 <= nums.length <= 10^5
  -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        # 양의 정수 갯수만큼 다 있어야 하니 len써도 됨.
        # +2인 이유는 2까지 있으면 3이 답이니까 체크해야함.
        for i in range(1, len(num_set) + 2):
            if i not in num_set:
                return i


inputdatas = [
    {"data": [[1, 2, 0]], "answer": 3},
    {"data": [[3, 4, -1, 1]], "answer": 2},
    {"data": [[7, 8, 9, 11, 12]], "answer": 1},
    {"data": [[-5]], "answer": 1}
]

"""
LeetCode Hard.
제출 3.3M, 정답률 40.3%
Hard치곤 상당히 쉬웠다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
