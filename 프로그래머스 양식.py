# https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
"""


def solution():
    return


inputdatas = [

]

"""
2022 카카오 테크 인턴십 기출. 
Lv.3. 현 시점 완료한 사람 1155명, 정답률 22%
"""

for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
