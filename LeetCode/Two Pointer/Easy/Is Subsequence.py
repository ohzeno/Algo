# https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1
from typing import Optional, List
"""
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
s가 t의 subsequence인지 여부를 리턴하시오.
subsequence: 원본의 순서는 유지되나, 중간에 빠진 문자가 있을 수 있음
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s > len_t:  # s가 t보다 길면 subsequence가 될 수 없음
            return False
        i = j = 0
        while i < len_s and j < len_t:  # 범위를 벗어나지 않는 동안
            if s[i] == t[j]:  # 일치하면 s 다음 문자로
                i += 1
            j += 1  # 찾았든 못찾았든 t는 다음 문자로 가야 함.
        return i == len_s  # s의 모든 문자를 찾았으면 i == len_s가 된다.
inputdatas = [
    ["abc", "ahbgdc"],
    ["axc", "ahbgdc"],
    ["acb", "ahbgdc"],
]

"""
LeetCode Easy.
내 초안과 다른 풀이들의 성능차이는 크게 없으나
다른 풀이들이 가독성이 좋아서 풀이를 수정했다.
초안도 다른 풀이들도 결국 투포인터다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
