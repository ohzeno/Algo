# https://leetcode.com/problems/valid-parentheses/
"""
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or stack.pop() + c not in ['()', '[]', '{}']:
                    return False
        return not stack

inputdatas = [
    "()", "()[]{}", "(]"
]

"""
LeetCode Easy. 전형적인 괄호 유효성 검사 문제.
for문을 사용해서 풀고 약간 개선을 더했다.
베스트 풀이를 보니 딕셔너리를 사용했다. 딕셔너리 풀이도 제출해봤는데
내 풀이보다 1ms 빠르지만 메모리를 0.1mb 더 사용했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))