# https://school.programmers.co.kr/learn/courses/30/lessons/12906
"""
주어진 배열에서 연속적으로 나타나는 숫자를 제거.
단, 원소 순서는 유지.
원소 크기: 0 이상 9 이하
"""


def solution(arr):
    prev = -1
    answer = []
    for a in arr:
        if a != prev:
            answer.append(a)
            prev = a
    return answer


inputdatas = [
    {"data": [[1, 1, 3, 3, 0, 1, 1]], "answer": [1, 3, 0, 1]},
    {"data": [[4, 4, 4, 3, 3]], "answer": [4, 3]},
]

"""
스택/큐
Lv.1. 현 시점 완료한 사람 68,483명, 정답률 77%
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
