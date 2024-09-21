# https://school.programmers.co.kr/learn/courses/30/lessons/12928
"""
constraints:
 - n은 0 이상 3000이하인 정수입니다.
"""


def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])


inputdatas = [
    {"data": [12], "answer": 28},
    {"data": [5], "answer": 6}
]


"""
연습문제
Lv.1. 현 시점 완료한 사람 72,181명, 정답률 88%
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
