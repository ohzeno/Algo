# https://leetcode.com/problems/merge-strings-alternately/
from typing import Optional, List
"""
constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i] + word2[i])
        return ''.join(ans) + word1[i+1:] + word2[i+1:]

inputdatas = [
    [['abc', 'pqr'], 'apbqcr'],
    [['ab', 'pqrs'], 'apbqrs'],
    [['abcd', 'pq'], 'apbqcd'],
]

"""
LeetCode Easy.
제출 557.2K, 정답률 79.1%
1분 30초쯤 썼다. 
문자열에 추가하는 방식을 썼는데
문자열이 불변객체라 매번 새로 생성하니 메모리 소모가 크다는 주장을 봤다.
같은 변수에 대한 업데이트라 가비지컬렉션이 작동하지 않을까 싶긴 한데
리스트에 추가하는 방식으로 풀어봤다.
메모리나 실행시간 변화는 딱히 없었다. 
문자열이 더 길어야 변화를 알 수 있을 지도 모르겠다. 
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for data, ans in inputdatas:
    if my_func(*data) == ans:
        print('pass')
    else:
        print('fail')
