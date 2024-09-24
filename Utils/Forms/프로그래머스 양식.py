# https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
constraints:
"""


def solution():
    return


inputdatas = [
    {"data": [], "answer": ""},
]

"""
2022 카카오 테크 인턴십 기출. 
Lv.3. 현 시점 완료한 사람 1155명, 정답률 22%
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
