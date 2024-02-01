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
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt_d = Counter(s)
        max_cnt = 0
        max_c = ''
        total = 0
        for c, cnt in cnt_d.items():
            total += cnt
            if cnt > max_cnt:
                max_cnt = cnt
                max_c = c
        remain = total - max_cnt
        if remain < max_cnt - 1:
            return ''
        parts = [max_c] * max_cnt
        i = 0
        for c, cnt in cnt_d.items():
            if c == max_c:
                continue
            for _ in range(cnt):
                parts[i] += c
                i = (i + 1) % max_cnt  # 돌아가면서 채워넣기
        return ''.join(parts)


inputdatas = [
    ["aab", "aba"],
    ["aaab", ""],
    ["vvvlo", "vlvov"],
    ['aaabcd', 'abacad'],
]

"""
LeetCode Medium.
제출 666.9K, 정답률 54.4%
빈도가 높은 문자를 먼저 채우고, 나머지 문자를 빈도가 높은 문자 사이에 채워넣는다.
최빈 문자의 빈도 - 1 보다 나머지 문자의 빈도의 합이 작으면 
최빈 문자들이 인접하는 경우가 생기므로 불가능하다.
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
