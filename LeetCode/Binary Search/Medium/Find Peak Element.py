# https://leetcode.com/problems/find-peak-element/
from typing import Optional, List

"""
constraints:
  1 <= nums.length <= 1000
  -2^31 <= nums[i] <= 2^31 - 1
  nums[i] != nums[i + 1] for all valid i.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ll, rr = 0, len(nums) - 1
        while ll < rr:
            mid = (ll + rr) // 2
            # mid+1이 더 크니 오른쪽으로 이동
            if nums[mid] < nums[mid + 1]:
                ll = mid + 1
            # mid가 더 크면 왼쪽으로 이동
            else:
                """
                mid, mid+1의 값이 같은 경우에 왼쪽으로 계속 이동하면 
                아래같은 케이스에 오류 생길 수 있는데,
                nums[i] != nums[i + 1] for all valid i 조건이 있어서 그런 케이스는 없다.
                {"data": [[1, 1, 1, 1, 2]], "answer": 4},
                """
                rr = mid
        return ll


inputdatas = [
    {"data": [[1, 2, 3, 1]], "answer": 2},
    {"data": [[1, 2, 1, 3, 5, 6, 4]], "answer": 5},
    {"data": [[1]], "answer": 0},
]

"""
LeetCode Medium.
제출 3.7M, 정답률 46.2%

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
