# https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""
constraints:

"""


def solution(arr1, arr2):
    Ar, Ac = len(arr1), len(arr1[0])
    Br, Bc = len(arr2), len(arr2[0])
    C = [[0] * Bc for _ in range(Ar)]
    for r in range(Ar):
        for c in range(Bc):
            C[r][c] = sum([arr1[r][k] * arr2[k][c] for k in range(Ac)])
    return C


inputdatas = [
    {"data": [[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]], "answer": [[15, 15], [15, 15], [15, 15]]},
    {"data": [[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]], "answer": [[22, 22, 11], [36, 28, 18], [29, 20, 14]]}
]


"""
연습문제
Lv.2. 현 시점 완료한 사람 25,477명, 정답률 67%
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
