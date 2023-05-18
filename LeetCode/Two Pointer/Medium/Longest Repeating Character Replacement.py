# https://leetcode.com/problems/longest-repeating-character-replacement/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_s = len(s)
        if len_s == 1:
            return len_s
        max_len = 0
        cnts = {}
        ll, rr = 0, 0
        while rr < len_s:
            cnts[s[rr]] = cnts.get(s[rr], 0) + 1
            while rr - ll + 1 - max(cnts.values()) > k:  # 길이 - 가장 많은 문자 갯수 = 바꿔야 하는 문자 갯수가 제한보다 많으면 ll 옮기기
                cnts[s[ll]] -= 1
                ll += 1
            max_len = max(max_len, rr - ll + 1)  # 기존 기록과 현재 길이 비교해서 최대 길이 갱신
            rr += 1
        return max_len


inputdatas = [
    ["ABAB", 2],
    ["AABABBA", 1],
]

"""
LeetCode Medium.
투 포인터로 풀었다.
슬라이딩 윈도우라고 하던데 이걸 그렇게 풀 수가 있나...?
슬라이딩 윈도우라고 주장하는 풀이들을 살펴보면 전부 투 포인터였다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
