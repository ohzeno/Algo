# https://leetcode.com/problems/simplify-path/
from typing import Optional, List

"""
constraints:
  • 1 <= path.length <= 3000
  • path consists of English letters, digits, period '.', slash '/' or '_'.
  • path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)


inputdatas = [
    {"data": ["/home/"], "answer": "/home"},
    {"data": ["/home//foo/"], "answer": "/home/foo"},
    {"data": ["/home/user/Documents/../Pictures"], "answer": "/home/user/Pictures"},
    {"data": ["/../"], "answer": "/"},
    {"data": ["/.../a/../b/c/../d/./"], "answer": "/.../b/d"}
]

"""
LeetCode Medium.
제출 2.2M, 정답률 47.2%
스택 아이디어만 떠올리면 쉬운 문제.
그렇지 못하면 split리스트 순회하며 if문들로 처리해줘야 한다.
그렇게 하더라도 풀다보면 '..'때문에 스택 떠올릴듯.
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
