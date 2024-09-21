# https://school.programmers.co.kr/learn/courses/30/lessons/12969
"""
constraints:

"""


# a, b = map(int, input().strip().split(' '))
def solution(n, m):
    return (n * "*" + "\n") * m

inputdatas = [
    {"data": [5, 3], "answer": "*****\n*****\n*****\n"},
]


"""
연습문제
Lv.1. 현 시점 완료한 사람 54,557명, 정답률 79%
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
