# https://leetcode.com/problems/backspace-string-compare/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspace(s) == self.backspace(t)

    def backspace(self, s: str) -> str:
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return ''.join(stack)

inputdatas = [
    ["ab#c", "ad#c"],
    ["ab##", "c#d#"],
    ["a#c", "b"],
    ["y#fo##f", "y#f#o##f"]
]

"""
LeetCode Easy.
평범한 스트링 문제. 스택을 사용해 풀었지만, 스택을 사용하지 않고도 풀린다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[1][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
