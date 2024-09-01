# https://school.programmers.co.kr/learn/courses/30/lessons/120875
"""
constraints:
  • dots의 길이 = 4
  • dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
    ◦ 0 ≤ x, y ≤ 100
  • 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
  • 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
  • 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.
"""


def solution(dots):
    def calc_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    combinations = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    for (a, b), (c, d) in combinations:
        slope1 = calc_slope(dots[a], dots[b])
        slope2 = calc_slope(dots[c], dots[d])
        if slope1 == slope2:
            return 1
    return 0


inputdatas = [
    {"data": [[[1, 4], [9, 2], [3, 8], [11, 6]]], "answer": 1},
    {"data": [[[3, 5], [4, 1], [2, 4], [5, 10]]], "answer": 0},
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 12,285명, 정답률 52%
점을 중첩해서 선택해도 되는지 안되는지 언급이 없어서 
언어지능 높은 사람은 오히려 시간 많이 쓸 수 있음.
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
