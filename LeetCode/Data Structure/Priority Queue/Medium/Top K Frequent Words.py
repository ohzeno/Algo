# https://leetcode.com/problems/top-k-frequent-words/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
빈도 내림차순 k개 단어 반환. 빈도가 같으면 사전순으로 반환
"""
from collections import Counter
from heapq import heapify, heappop as hpop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        # return sorted(list(cnt), key=lambda x: (-cnt[x], x))[:k]
        heap = [(-val, key) for key, val in cnt.items()]
        heapify(heap)
        return [hpop(heap)[1] for _ in range(k)]


inputdatas = [
    [["i", "love", "leetcode", "i", "love", "coding"], 2],
    [["love", "i", "leetcode", "i", "love", "coding"], 2],
    [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
    [["i","love","leetcode","i","love","coding"], 3],
]

"""
LeetCode Medium.
처음엔 most_common을 사용한 후 사전순으로 다시 정렬해서 통과했다.
생각해보니 어차피 또 정렬할거면 most_common을 사용할 필요가 없었다.
heap 카테고리의 문제였으니 heapq로도 풀었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
