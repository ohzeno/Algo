# https://leetcode.com/problems/longest-palindromic-substring/
"""
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        wleng, sleng = 1, len(s)
        ans = s[0]
        for i in range(sleng - 1):  # 각 지점 순회
            for j in range(i+wleng, sleng+1):  # 최소 길이부터 s 끝까지 순회
                forward = s[i:j]
                backward = forward[::-1]
                if forward == backward:  # 팰린드롬이면
                    if wleng < j - i:  # 기존보다 더 길면
                        wleng = j - i  # 길이 갱신
                        ans = forward  # 답 갱신
        return ans

inputdatas = [
    "babad",
    "cbbd",
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Medium. 2중 for문을 사용했다.
더 효율적인 풀이들을 살펴봤으나 직관적이지 못해서 일단 넘어간다.
"""
