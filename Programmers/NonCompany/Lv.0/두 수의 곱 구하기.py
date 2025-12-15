# https://school.programmers.co.kr/learn/courses/30/lessons/120804?language=python3
"""
constraints:

"""


def solution(num1, num2):
    return num1 * num2


inputdatas = [
    {"data": [3, 4], "answer": 12},
    {"data": [27, 19], "answer": 513}
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 100,022명, 정답률 92%
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
