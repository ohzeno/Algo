# https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""
constraints:

"""


def solution(routes):
    # routes[i] = i번째 차량의 고속도로 [진입, 이탈 지점]
    # 진입, 이탈 지점 카메라도 만난 것.
    # 인터벌 머지?
    routes.sort(key=lambda x: x[1])
    prev_ed = -30001
    camera_cnt = 0
    for st, ed in routes:
        # 이전 ed에 설치했다고 가정.
        if prev_ed < st:
            prev_ed = ed
            camera_cnt += 1
    return camera_cnt


inputdatas = [
    {"data": [[[-20, -15], [-14, -5], [-18, -13], [-5, -3]]], "answer": 2},
    {"data": [[[0, 12], [1, 12], [2, 12], [3, 12], [5, 6], [6, 12], [10, 12]]], "answer": 2},
    {"data": [[[-2, -1], [1, 2], [-3, 0]]], "answer": 2},
    {"data": [[[0, 0], ]], "answer": 1},
    {"data": [[[0, 1], [0, 1], [1, 2]]], "answer": 1},
    {"data": [[[0, 1], [2, 3], [4, 5], [6, 7]]], "answer": 4},
    {"data": [[[-20, -15], [-14, -5], [-18, -13], [-5, -3]]], "answer": 2},
    {"data": [[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]], "answer": 2},
    {"data": [[[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]], "answer": 2},
    {"data": [[[-7, 0], [-6, -4], [-5, -3], [-3, -1], [-1, 4], [1, 2], [3, 4]]], "answer": 4},
    {"data": [[[-5, -3], [-4, 0], [-4, -2], [-1, 2], [0, 3], [1, 5], [2, 4]]], "answer": 2},
]

"""
탐욕법(Greedy)
Lv.3. 현 시점 완료한 사람 18,479명, 정답률 58%
Interval Scheduling 문제.
Interval Merge로 착각해서 한번 틀렸다.
st기준 정렬해서 Merge하면 0, 10에서 10에 설치하면 1, 9가 오면 그룹은 같지만 단속안됨.
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
