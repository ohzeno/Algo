# https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""
문자열 s에 나타나는 숫자 중 최솟값, 최댓값을 찾아 "최솟값 최댓값" 형태로 return
s에는 둘 이상의 정수가 공백으로 구분되어 있음
"""


def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"


inputdatas = [
    {"data": ["1 2 3 4"], "answer": "1 4"},
    {"data": ["-1 -2 -3 -4"], "answer": "-4 -1"},
    {"data": ["-1 -1"], "answer": "-1 -1"},
]

"""
최댓값과 최솟값
Lv.2. 현 시점 완료한 사람 41352명, 정답률 79%
이게 Lv.2...? 카카오 Lv.1 정답률 23% 문제에 머리쓰고 이거 보니 어이가 없다.
split 안쓰고 풀어도 Lv.2는 좀 아니지 않나 싶다. 레벨 기준이 도대체 뭐지...?
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
