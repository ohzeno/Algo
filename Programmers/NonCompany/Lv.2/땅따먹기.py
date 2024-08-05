# https://school.programmers.co.kr/learn/courses/30/lessons/12913
"""
n행 4열 땅. 한 행씩 밟으며 내려올 때, 같은 열을 연속해서 밟을 수 없다.
각 행의 4개 숫자 중 하나를 선택하여 밟을 때, 밟은 숫자의 합의 최대값을 리턴하라
행 개수 n: 10만 이하 자연수
"""


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][k] for k in range(4) if k != j])
    return max(land[-1])

inputdatas = [
    {"data": [[[1,2,3,5],[5,6,7,8],[4,3,2,1]]], "answer": 16},
]

"""
연습문제
Lv.2. 현 시점 완료한 사람 14,821명, 정답률 59%
간단한 dp문제.
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
