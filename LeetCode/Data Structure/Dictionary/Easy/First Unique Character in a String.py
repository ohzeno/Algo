# https://leetcode.com/problems/first-unique-character-in-a-string/
from typing import Optional, List

"""
constraints:
  • 1 <= s.length <= 10^5
  • s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnts = {}
        for ch in s:
            cnts[ch] = cnts.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if cnts[ch] == 1:
                return i
        return -1


inputdatas = [
    {"data":["leetcode"], "answer": 0},
    {"data":["loveleetcode"], "answer": 2},
    {"data":["aabb"], "answer": -1},
]

"""
LeetCode Easy.
제출 3.3M, 정답률 64.3%

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
