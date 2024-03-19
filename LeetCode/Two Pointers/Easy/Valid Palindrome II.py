# https://leetcode.com/problems/valid-palindrome-ii/description/
from typing import Optional, List

"""
Given a string s, return true if the s can be palindrome 
after deleting at most one character from it.
constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.is_palindrome(s):
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                del_left = s[l+1:r+1]
                del_right = s[l:r]
                return self.is_palindrome(del_left) or self.is_palindrome(del_right)
            l += 1
            r -= 1
        return True


inputdatas = [
    {"data": ["aba"], "answer": True},
    {"data": ["abca"], "answer": True},
    {"data": ["abc"], "answer": False},
    {"data": ["a"], "answer": True},
]

"""
LeetCode Easy.
제출 1.8M, 정답률 40.4%
Easy치고는 어렵다. Editorial 반응들도 Medium 아니냐고 아우성.
단순하게 생각하면 투포인터로 좁혀가면서 일치하지 않는 문자가 나오면 
한쪽씩 제거하여서 펠린드롬 검사를 하는 것이다.
10^5라 그렇게 하면 문제가 생길 수 있다.
좁혀온 부분은 이미 펠린드롬이니 다시 검사할 필요가 없다. 
즉, 안쪽만 검사하면 되기에 문자를 제거할 필요 없이 안쪽 인덱싱만으로 체크할 수 있다.
"""
import inspect
functions = [
    value for value in Solution.__dict__.values() if inspect.isfunction(value)
]
my_func = functions[1]
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
