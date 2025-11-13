# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
from typing import Optional, List

"""
constraints:
  • 2 <= s.length <= 1000
  • s[i] is either 'L' or 'R'.
  • s is a balanced string.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        p = 0
        for ch in s:
            if ch == 'L':
                p += 1
            else:
                p -= 1
            if p == 0:
                cnt += 1
        return cnt


inputdatas = [
    {"data": ["RLRRLLRLRL"], "answer": 4},
    {"data": ["RLRRRLLRLL"], "answer": 2},
    {"data": ["LLLLRRRR"], "answer": 1}
]

"""
LeetCode Easy.
제출 419.9K, 정답률 87.1%

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
