# https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""
constraints:
  • array의 길이는 1 이상 100 이하입니다.
  • array의 각 원소는 1 이상 100 이하입니다.
  • commands의 길이는 1 이상 50 이하입니다.
  • commands의 각 원소는 길이가 3입니다.
"""


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        part = array[i-1:j]
        part.sort()
        answer.append(part[k-1])
    return answer


inputdatas = [
    {"data": [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]], "answer": [5, 6, 3]}
]


"""
정렬
Lv.1. 현 시점 완료한 사람 103,398명, 정답률 72%
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
