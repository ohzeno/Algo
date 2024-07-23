# https://leetcode.com/problems/majority-element/
from typing import Optional, List

"""
constraints:
  n == nums.length
  1 <= n <= 5 * 10^4
  -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


inputdatas = [
    {"data": [[3,2,3]], "answer": 3},
    {"data": [[2,2,1,1,1,2,2]], "answer": 2}
]

"""
LeetCode Easy.
제출 4.8M, 정답률 65.0%%
최빈값을 찾는 거라 카운터를 쓰려고 했는데
정확히는 'n/2' 이상으로 출현하는 값이다.
정렬을 하면 위 값은 절반 이상의 길이이므로 어디에 위치하든 
n//2 인덱스에 걸쳐질 수 밖에 없다.
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
