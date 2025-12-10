# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import Optional, List

"""
constraints:
  • 0 <= nums.length <= 10^5
  • -10^9 <= nums[i] <= 10^9
"""


class Solution:
    # 정렬 풀이
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        max_len = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                length += 1
                max_len = max(max_len, length)
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = 1
        return max_len

    # 해시 풀이
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + 1 in num_set:
                    num += 1
                    length += 1
                max_len = max(max_len, length)
        return max_len


inputdatas = [
    {"data": [[100, 4, 200, 1, 3, 2]], "answer": 4},
    {"data": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "answer": 9},
    {"data": [[1, 0, 1, 2]], "answer": 3},
    {"data": [[]], "answer": 0},
]

"""
LeetCode Medium.
제출 6.1M, 정답률 47.0%
처음에 정렬로 풀었는데 O(log n)은 10 이후로 O(1)보다 크다.
즉, O(n log n)은 O(n)보다 대부분 크다.
정렬 풀이도 시간초과는 안하지만 O(n) 풀이도 만들었다.
O(n)풀이는 set를 iterable로 사용해서 자료구조 측면으로는 직관성이 많이 떨어지긴 한다.
10년 전 파이썬에서도 set 순회가 가능했다는걸 처음 알았다.
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
