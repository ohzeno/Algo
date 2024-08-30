# https://school.programmers.co.kr/learn/courses/30/lessons/120805
"""
constraints:
  • 0 < num1 ≤ 100
  • 0 < num2 ≤ 100
"""


def solution(num1, num2):
    return num1 // num2


inputdatas = [
    {"data": [10, 5], "answer": 2},
    {"data": [7, 2], "answer": 3}
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 73,833명, 정답률 91%
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
