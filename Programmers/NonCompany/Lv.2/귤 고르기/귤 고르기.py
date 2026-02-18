# https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=python3
"""
constraints:
  • 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
  • 1 ≤ tangerine의 원소 ≤ 10,000,000
"""

from collections import Counter

def solution(k, tangerine):
    cnt_d = Counter(tangerine)
    tot = 0
    types = 0
    for cnt in sorted(cnt_d.values(), reverse=True):
        tot += cnt
        types += 1
        if tot >= k:
            return types


inputdatas = [
    {"data": [6, [1, 3, 2, 5, 4, 5, 2, 3]], "answer": 3},
    {"data": [4, [1, 3, 2, 5, 4, 5, 2, 3]], "answer": 2},
    {"data": [2, [1, 1, 1, 1, 2, 2, 2, 3]], "answer": 1}
]


"""
연습문제
Lv.2. 현 시점 완료한 사람 24,561명, 정답률 72%
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
