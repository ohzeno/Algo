# https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""
constraints:
  • sizes의 길이는 1 이상 10,000 이하입니다.
    ◦ sizes의 원소는 [w, h] 형식입니다.
    ◦ w는 명함의 가로 길이를 나타냅니다.
    ◦ h는 명함의 세로 길이를 나타냅니다.
    ◦ w와 h는 1 이상 1,000 이하인 자연수입니다.
"""


def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h


inputdatas = [
    {"data": [[[60, 50], [30, 70], [60, 30], [80, 40]]], "answer": 4000},
    {"data": [[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]], "answer": 120},
    {"data": [[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]], "answer": 133}
]


"""
완전탐색
Lv.1. 현 시점 완료한 사람 53,562명, 정답률 75%
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
