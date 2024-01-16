# https://leetcode.com/problems/group-anagrams/description/
from typing import Optional, List
"""
스트링 어레이가 주어지면 애너그램을 그룹화하라.
정렬은 상관없다.
constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())


inputdatas = [
    [["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]],
    [[""], [[""]]],
    [["a"], [["a"]]],
]

"""
LeetCode Medium.
제출 3.7M, 정답률 67.4%
애너그램 정의를 단어를 뒤집은 것으로 착각하고 풀었다가 한 번 틀렸다.
문제를 다시 읽고 풀었고, 최종적으로 6분만에 해결됐다.
set를 사용하면 더 편할 것 같긴 했는데 그러면 key값으로 사용하기 까다롭다.
혹시나 더 좋은 풀이가 있을까 살펴봤는데 내 풀이가 99% 이상을 beat했고 
더 빠른 풀이도 로직은 같았다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(data)
    for r in res:
        r.sort()
    for a in answer:
        a.sort()
    res.sort()
    answer.sort()
    if res == answer:
        print('pass')
    else:
        print('fail\n', f'expected:{answer}\n', f'got:{res}\n')
