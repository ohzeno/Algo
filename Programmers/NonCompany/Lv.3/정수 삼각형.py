# https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""
피보나치처럼 삼각형 형태로 배치된 숫자들.
꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합의 최댓값을 리턴하라.
제한사항
    삼각형의 높이는 1 이상 500 이하입니다.
    삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
"""


def solution(tri):
    for i in range(1, len(tri)):
        for j in range(i + 1):
            if j == 0:
                tri[i][j] = tri[i-1][j] + tri[i][j]
            elif i == j:
                tri[i][j] = tri[i-1][j-1] + tri[i][j]
            else:
                tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
    return max(tri[-1])


inputdatas = [
    {
        "data": [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]],
        "answer": 30
    },
]

"""
정수 삼각형. 동적계획법(Dynamic Programming)
Lv.3. 현 시점 완료한 사람 23944명, 정답률 60%
그냥 tri 자체를 dp로 써도 된다.
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
