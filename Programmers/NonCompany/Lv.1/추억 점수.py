# https://school.programmers.co.kr/learn/courses/30/lessons/176963
"""
constraints:
  • 3 ≤ name의 길이 = yearning의 길이≤ 100
    ◦ 3 ≤ name의 원소의 길이 ≤ 7
    ◦ name의 원소들은 알파벳 소문자로만 이루어져 있습니다.
    ◦ name에는 중복된 값이 들어가지 않습니다.
    ◦ 1 ≤ yearning[i] ≤ 100
    ◦ yearning[i]는 i번째 사람의 그리움 점수입니다.
  • 3 ≤ photo의 길이 ≤ 100
    ◦ 1 ≤ photo[i]의 길이 ≤ 100
    ◦ 3 ≤ photo[i]의 원소(문자열)의 길이 ≤ 7
    ◦ photo[i]의 원소들은 알파벳 소문자로만 이루어져 있습니다.
    ◦ photo[i]의 원소들은 중복된 값이 들어가지 않습니다.
"""


def solution(name, yearning, photo):
    yearning_d = dict(zip(name, yearning))
    ans = []
    for p in photo:
        score = 0
        for name in p:
            score += yearning_d.get(name, 0)
        ans.append(score)
    return ans

inputdatas = [
    {
        "data": [
            ["may", "kein", "kain", "radi"],
            [5, 10, 1, 3],
            [
                ["may", "kein", "kain", "radi"],
                ["may", "kein", "brin", "deny"],
                ["kon", "kain", "may", "coni"],
            ],
        ],
        "answer": [19, 15, 6],
    },
    {
        "data": [
            ["kali", "mari", "don"],
            [11, 1, 55],
            [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]],
        ],
        "answer": [67, 0, 55],
    },
    {
        "data": [
            ["may", "kein", "kain", "radi"],
            [5, 10, 1, 3],
            [["may"], ["kein", "deny", "may"], ["kon", "coni"]],
        ],
        "answer": [5, 15, 0],
    },
]


"""
연습문제
Lv.1. 현 시점 완료한 사람 25,785명, 정답률 69%
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
