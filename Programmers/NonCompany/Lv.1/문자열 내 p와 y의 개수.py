# https://school.programmers.co.kr/learn/courses/30/lessons/12916
"""
"""


def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")


inputdatas = [
    {"data": ["pPoooyY"], "answer": True},
    {"data": ["Pyy"], "answer": False},
]

"""
연습문제
Lv.1. 현 시점 완료한 사람 61,356명, 정답률 87%
브랜치에서 커밋한게 몇 있긴 한데, merge하기엔 기능 완성이 안되어서,
병합하기 전까지는 오늘 커밋 잔디가 비어있을 것 같았다.
어차피 병합하면 채워질거긴 한데 임시로라도 잔디 채우기 위해 급하게 풀었다.
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
