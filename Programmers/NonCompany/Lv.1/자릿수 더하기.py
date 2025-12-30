# https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3
"""
constraints:
  • N의 범위 : 100,000,000 이하의 자연수
"""


def solution(n):
    n = str(n)
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])
    return ans

inputdatas = [
    {"data": [123], "answer": 6},
    {"data": [987], "answer": 24}
]


"""
연습문제
Lv.1. 현 시점 완료한 사람 80,003명, 정답률 88%
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
