# https://leetcode.com/problems/longest-palindrome/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        tmp = sum([v // 2 * 2 for v in cnt.values()])  # 아래 주석 참고
        return tmp + 1 if tmp < len(s) else tmp

inputdatas = [
    "abccccdd",
    "a",
]

"""
LeetCode Easy.
처음에 문제를 너무 어렵게 생각했다.
Counter를 사용하면 간단하게 풀 수 있다.
val을 //2로 나누면 짝이 있는 쌍만 남는다. 거기에 *2를 해주면 펠린드롬에 사용할 수 있는 문자 갯수만 남는다.
그 값을 다 더했을 때, len(s)보다 작으면 홀수 개 문자가 남아있다는 뜻이다.
홀수 문자는 중앙에 더해줄 수 있으므로 +1.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
