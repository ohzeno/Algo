# https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""
constraints:
  • 5 ≤ s의 길이 ≤ 50
  • 1 ≤ skip의 길이 ≤ 10
  • s와 skip은 알파벳 소문자로만 이루어져 있습니다.
    ◦ skip에 포함되는 알파벳은 s에 포함되지 않습니다.
  • 1 ≤ index ≤ 20
"""


def solution(s, skip, index):
    new_s = ""
    alp = set('abcdefghijklmnopqrstuvwxyz') - set(skip)
    alp = sorted(alp)
    l_alp = len(alp)
    alp2i = {c: i for i, c in enumerate(alp)}
    for i, c in enumerate(s):
        new_i = (alp2i[c] + index) % l_alp
        new_s += alp[new_i]
    return new_s



inputdatas = [
    {"data": ["aukks", "wbqd", 5], "answer": "happy"}
]


"""
연습문제
Lv.1. 현 시점 완료한 사람 14,914명, 정답률 58%
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
