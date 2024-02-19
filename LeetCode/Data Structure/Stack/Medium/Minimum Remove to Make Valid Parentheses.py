# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
from typing import Optional, List

"""
최소한의 괄호를 제거해서 모든 괄호가 유효하도록 만들어라.
constraints:
1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)


inputdatas = [
    ["lee(t(c)o)de)", "lee(t(c)o)de"],
    ["a)b(c)d", "ab(c)d"],
    ["))((", ""],
]

"""
LeetCode Medium.
제출 846.9K, 정답률 67.0%
괄호 유효성 검사 후 불필요한 괄호 제거하는 문제.
s를 리스트로 변환하면 편하다.
( 좌표를 스택에 넣고 매칭되지 않는 )는 빈 문자열로 교체,
스택에 남아있는 (도 매칭되지 않으므로 빈 문자열로 교체.
최종적으로 리스트 join해서 리턴.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
