# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
"""
constraints:

"""


def solution(answers):
    ss = [
        (5, [1, 2, 3, 4, 5]),
        (8, [2, 1, 2, 3, 2, 4, 2, 5]),
        (10, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    p = [0, 0, 0]
    for i, correct_answer in enumerate(answers):
        for j in range(3):
            n, sal = ss[j]
            p[j] += int(sal[i % n] == correct_answer)
    max_p = max(p)
    return [i for i, s in enumerate(p, 1) if s == max_p]


inputdatas = [
    {"data": [[1,2,3,4,5]], "answer": [1]},
    {"data": [[1,3,2,4,2]], "answer": [1,2,3]}
]


"""
완전탐색
Lv.1. 현 시점 완료한 사람 85,174명, 정답률 66%
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
