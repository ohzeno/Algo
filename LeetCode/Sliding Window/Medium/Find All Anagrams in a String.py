# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        len_s, len_p = len(s), len(p)
        p = sorted(p)
        if len_s < len_p:
            return ans
        for i in range(len_s - len_p + 1):
            if sorted(s[i:i+len_p]) == p:
                ans.append(i)
        return ans


inputdatas = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"]
]

"""
LeetCode Medium.
슬라이딩 윈도우 문제. 
나는 sorted로 풀었는데, 시간복잡도를 줄이고 싶다면 Counter나 dict로 푸는 방법도 있다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
