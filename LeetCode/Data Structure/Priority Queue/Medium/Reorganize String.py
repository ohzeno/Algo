# https://leetcode.com/problems/reorganize-string/
from typing import Optional, List
"""
constraints:
1 <= s.length <= 500
s consists of lowercase English letters.

s가 주어지면 인접한 문자끼리 같지 않도록 재정렬하여 반환하라.
만약 불가능하면 빈 문자열을 반환하라.
"""
from collections import Counter
from heapq import heappush as hpush, heappop as hpop
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt_d = Counter(s)
        q = []
        for c, cnt in cnt_d.items():
            hpush(q, (-cnt, c))
        res = ''
        while len(q) > 1:
            cnt1, c1 = hpop(q)
            cnt2, c2 = hpop(q)
            res += c1 + c2
            if abs(cnt1) - 1 > 0:
                hpush(q, (cnt1 + 1, c1))
            if abs(cnt2) - 1 > 0:
                hpush(q, (cnt2 + 1, c2))
        if q:
            cnt, c = hpop(q)
            if abs(cnt) > 1:
                return ''
            res += c
        return res


inputdatas = [
    ["aab", "aba"],
    ["aaab", ""],
    ["vvvlo", "vlvov"],
    ['aaabcd', 'abacad'],
]

"""
LeetCode Medium.
제출 666.9K, 정답률 54.4%
우선순위 큐를 사용할 경우
q에 둘 이상이 있는 동안 빈도가 제일 높은 둘을 뽑아서 문자열에 추가한다.
c2가 다음 c1이 올 가능성이 떠오를 수 있는데,
우선순위 큐라 c1이 항상 빈도가 더 높다. 둘 다 1씩 줄어들어도 c1이 더 클 것이라
c2가 다음 c1이 될 수 없어서 괜찮다.
마지막에 q에 남은 문자가 있을 경우, 빈도가 1이 아니면 인접하므로 불가능한 경우이다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(data)
    if res == answer:
        print('pass')
    else:
        print('fail\n', f'expected:{answer}\n', f'got:{res}\n')
