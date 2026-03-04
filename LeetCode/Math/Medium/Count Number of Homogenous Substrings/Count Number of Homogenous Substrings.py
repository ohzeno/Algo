# https://leetcode.com/problems/count-number-of-homogenous-substrings/
from typing import Optional, List

"""
constraints:
  • 1 <= s.length <= 10^5
  • s consists of lowercase letters.
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = int(1e9) + 7
        tot = 1
        n = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n += 1
            else:
                n = 1
            tot = (tot + n) % MOD
        return tot


inputdatas = [
    {"data": ["abbcccaa"], "answer": 13},
    {"data": ["xy"], "answer": 2},
    {"data": ["zzzzz"], "answer": 15}
]

"""
LeetCode Medium.
제출 228.8K, 정답률 57.4%
패턴을 찾아보면 2글자면 3개, 3글자면 6, 4글자면 10. 매번 'n'글자가 더해진다.
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
