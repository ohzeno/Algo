# https://leetcode.com/problems/decode-string/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':  # 닫으면 연산
                word = stack.pop()  # 반복할 문자열
                while stack and stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()  # '[' 제거
                num = ''  # 반복 횟수
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * word)  # 반복 횟수 * 문자열
            else:  # 닫힘 아니면 다 넣어줌
                stack.append(c)
        return ''.join(stack)


inputdatas = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
]

"""
LeetCode Medium.
while 안써보려고 고생했는데 결국 while이 제일 직관적이라 회귀했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
