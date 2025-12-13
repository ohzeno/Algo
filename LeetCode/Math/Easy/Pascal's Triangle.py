# https://leetcode.com/problems/pascals-triangle/
from typing import Optional, List

"""
constraints:
  • 1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            prev = pascal[i-1]
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            pascal.append(row)
        return pascal


inputdatas = [
    {"data": [5], "answer": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]},
    {"data": [1], "answer": [[1]]}
]

"""
LeetCode Easy.
제출 3.1M, 정답률 78.2%

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
