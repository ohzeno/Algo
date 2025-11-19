# https://leetcode.com/problems/valid-palindrome/
from typing import Optional, List

"""
constraints:
  • 1 <= s.length <= 2 * 10^5
  • s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtered = ''.join(c for c in s.lower() if c.isalnum())
        filtered = ''.join(filter(str.isalnum, s.lower()))
        return filtered == filtered[::-1]


inputdatas = [
    {"data": ["A man, a plan, a canal: Panama"], "answer": True},
    {"data": ["race a car"], "answer": False},
    {"data": [" "], "answer": True}
]

"""
LeetCode Easy.
제출 9.1M, 정답률 51.9%
isalnum을 처음 알았다.
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
