# https://leetcode.com/problems/valid-anagram/
from typing import Optional, List

"""
constraints:
  • 1 <= s.length, t.length <= 5 * 10^4
  • s and t consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter(t)
        for ch in s:
            cnt[ch] -= 1
            if cnt[ch] < 0:
                return False
        return True


inputdatas = [
    {"data": ["anagram", "nagaram"], "answer": True},
    {"data": ["rat", "car"], "answer": False}
]

"""
LeetCode Easy.
제출 7.9M, 정답률 67.2%

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
