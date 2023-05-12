# https://leetcode.com/problems/longest-common-prefix/
"""
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        # shortest = min(strs, key=len)  # 가장 짧은 문자열
        # for i, cur in enumerate(shortest):
        #     if any([s[i] != cur for s in strs]):  # 현 위치 문자열이 다른 원소가 있으면 ans 리턴.
        #         return ans
        #     ans += cur  # 다 같으면 ans에 추가.
        for tup in list(zip(*strs)):  # zip(*strs)는 각 원소의 i번째 문자열을 튜플로 묶어준다. 리스트에 사용할 때처럼.
            if len(set(tup)) != 1:  # 현 자리 원소가 모두 같지 않으면 ans 리턴.
                return ans
            ans += tup[0]  # 모두 같으면 ans에 추가.
        return ans

inputdatas = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    ["reflower","flow","flight"]
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Easy.
6분만에 풀고 이후는 개선 작업 했다. min과 any를 사용하여 간결하게 만들었다.
zip을 사용한 풀이를 봤는데 내 풀이보다 성능은 약간 부족하지만 훨씬 간결했다.
두 풀이 모두 pythonic한 풀이다.
나중에 알았는데 Trie를 사용해 풀 수도 있다.
"""
