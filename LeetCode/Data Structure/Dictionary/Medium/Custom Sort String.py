# https://leetcode.com/problems/custom-sort-string/
from typing import Optional, List

"""
constraints:
  • 1 <= order.length <= 26
  • 1 <= s.length <= 200
  • order and s consist of lowercase English letters.
  • All the characters of order are unique.
"""
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt_s = Counter(s)
        # 순서 있는 문자부터 정렬
        ans = [c * cnt_s.pop(c, 0) for c in order]
        # 순서 없는 문자 추가
        for c, n in cnt_s.items():
            ans.append(c * n)
        return "".join(ans)


inputdatas = [
    {"data": ["cba", "abcd"], "answer": "cbad"},
    {"data": ["bcafg", "abcd"], "answer": "bcad"},
    {"data": ["kqep", "pekeq"], "answer": "kqeep"},
]

"""
LeetCode Medium.
제출 723.5K, 정답률 71.9%
처음엔 교집합과 차집합 사용했으나 s는 unique하지 않음을 확인하고 counter 도입.
풀고 나서 다른 풀이 보니 Counter에도 pop이 있어서 풀이 개선
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
