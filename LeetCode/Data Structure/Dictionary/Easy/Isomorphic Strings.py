# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        vals = set()
        for n1, n2 in zip(s, t):
            if n1 in dic:  # n1이 이미 dic에 있으면
                if dic[n1] != n2:  # 대응문자와 다르면 False
                    return False
            else:  # n1이 dic에 없으면
                if n2 in vals:  # 대응문자가 이미 vals에 있으면 False. 두 문자가 한 문자에 매핑될 수 없다는 조건 때문.
                    return False
                dic[n1] = n2  # 대응문자 기록
                vals.add(n2)  # 대응문자를 vals에 추가
        return True  # 모든 문자가 대응되었으면 True

inputdatas = [
    ["egg", "add"],
    ["foo", "bar"],
    ["paper", "title"],
]

"""
LeetCode Easy.
처음엔 enumerate를 썼으나, 다른 풀이를 보고 zip으로 바꿨다.
대충 구현해서 통과하고 더 간결한 풀이가 없을까 살펴봤는데 
다른 풀이들도 내 풀이와 로직이 같았다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
