# https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
constraints:
  • 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
  • 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
  • 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
"""
import math

def solution(brown, yellow):
    total = brown + yellow
    # -> ceil로 제곱근 이상부터 탐색해서 w가 무조건 크도록 최적화
    for w in range(math.ceil(total ** 0.5), brown//2+1):
        if total % w == 0:
            h = (brown - 2 * w)//2 + 2
            inner_cells = (w-2) * (h-2)
            if inner_cells == yellow:
                return [w, h]


inputdatas = [
    {"data": [10, 2], "answer": [4, 3]},
    {"data": [8, 1], "answer": [3, 3]},
    {"data": [24, 24], "answer": [8, 6]}
]


"""
완전탐색
Lv.2. 현 시점 완료한 사람 57,663명, 정답률 73%
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
