# https://leetcode.com/problems/bag-of-tokens/
from typing import Optional, List

"""
constraints:
  • 0 <= tokens.length <= 1000
  • 0 <= tokens[i], power < 10^4
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ll, rr = 0, len(tokens) - 1
        score = 0
        while ll <= rr:
            # Face-up: get score
            if power >= tokens[ll]:
                power -= tokens[ll]
                score += 1
                ll += 1
            # Face-down: get power
            # ll == rr일 때는 power 얻는 게 의미 없음
            elif score >= 1 and ll < rr:
                power += tokens[rr]
                score -= 1
                rr -= 1
            else:
                break
        return score


inputdatas = [
    {"data": [[], 85], "answer": 0},
    {"data": [[100], 50], "answer": 0},
    {"data": [[200, 100], 150], "answer": 1},
    {"data": [[100, 200, 300, 400], 200], "answer": 2}
]

"""
LeetCode Medium.
제출 441K, 정답률 59.5%

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
