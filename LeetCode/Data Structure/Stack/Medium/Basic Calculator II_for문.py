# https://leetcode.com/problems/basic-calculator-ii/
from typing import Optional, List

"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') 
    separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers 
    in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def calculate(self, s: str) -> int:
        s = '+' + s.replace(" ", "")
        stack = []
        i, l_s = 0, len(s)
        while i < l_s:
            if s[i].isdigit():
                st = i
                while i+1 < l_s and s[i+1].isdigit():
                    i += 1
                num = int(s[st:i+1])
                match s[st-1]:
                    case "+":
                        stack.append(num)
                    case "-":
                        stack.append(-num)
                    case "*":
                        stack[-1] *= num
                    case "/":
                        stack[-1] = int(stack[-1] / num)
            i += 1
        return sum(stack)


inputdatas = [
    {"data": ["3+2*2"], "answer": 7},
    {"data": [" 3/2 "], "answer": 1},
    {"data": [" 3+5 / 2 "], "answer": 5},
    {"data": ["1-1+1"], "answer": 1},
    {"data": ["14-3/2"], "answer": 13},
    {"data": ["10000-1000/10+100*1"], "answer": 10000},
]

"""
LeetCode Medium.
제출 1.4M, 정답률 43.5%
첫 풀이는 *, /만 미리 연산하고 나머지는 스택에 넣어놓고
나중에 스택을 순회하면서 계산했다.
다른 풀이를 보니 더 간결한 풀이가 있어 수정해봤다.
다른 풀이는 replace를 사용하지 않고 while 대신 for문을 사용한다.
-에 대해 -num을 append하는 경우 
분모에 음수가 들어갈 수 있어 // 대신 int를 사용해야 한다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
