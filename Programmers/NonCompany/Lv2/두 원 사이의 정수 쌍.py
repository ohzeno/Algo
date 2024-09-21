# https://school.programmers.co.kr/learn/courses/30/lessons/181187
"""
반지름 둘이 주어질 때
직교좌표계에서 두 원 사이의 공간에 x, y 좌표가 모두 정수인 점 개수를 return하라.
원 위의 점도 포함한다.
1 ≤ r1 < r2 ≤ 1,000,000
"""
import math

def solution(r1, r2):
    cnt = 0
    r1_square = r1**2
    r2_square = r2**2
    for x in range(1, r2 + 1):
        x_square = x**2
        y1 = math.ceil(math.sqrt(max(r1_square - x_square, 0)))
        y2 = math.floor(math.sqrt(r2_square - x_square))
        cnt += y2 - y1 + 1
    return cnt * 4


inputdatas = [
    {"data": [2, 3], "answer": 20},
]

"""
연습문제
Lv.2. 현 시점 완료한 사람 5,662명, 정답률 39%
정답률을 보면 알겠지만 lv.2치고는 까다로운 문제.
lv2니까 당연히 2중for문 사용했다가 시간초과 발생.

1차 최적화로 전체 원을 계산하지 않고 아닌 4등분
(1사분면에서 y축만 제거. 축 제거해야 4배했을 때 중복 없음)된 원에서만 계산해야 한다.
그래도 2중for문에서 시간초과.

2차 최적화로 x에 따른 허용 구역의 y좌표 범위를 구해야 한다.
범위를 구한 후에 또 for문 쓰면 시간초과.
최고점, 최저점 있고 정수 갯수 구하는거니 그냥 갯수 구해서 더해준다.
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
