# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll, rr = 0, 0
        max_len = 0
        while rr < len(s):
            if s[rr] in s[ll:rr]:  # 유니크하지 않으면 왼쪽 포인터를 옮긴다.
                ll += 1
            else:  # 유니크하면 오른쪽 포인터를 옮기고 최대 길이를 갱신한다.
                rr += 1
                max_len = max(max_len, rr-ll)
        return max_len

inputdatas = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Medium. 
투포인터로 푸는데 3분쯤 걸렸다.
더 나은 풀이들을 보려 했는데 대부분 딕셔너리에 기록하면서 진행했다.
코드도 길고 설명도 길어서 그냥 넘어갔다.
"""
