# https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""
constraints:

"""


def solution(dartResult):
    """
    S D T 각 1 2 3제곱. 점수마다 존재함
    *: 현, 이전 점수 2배로 (첫 시도에 나오면 현 점수만 2배)
    *: 중첩 가능. 중첩은 4배
    #: 현 점수 마이너스. *과 중첩되면 -2배
    *과 #은 점수마다 둘 중 하나만 존재하거나 존재X
    f'{점수}{보너스}{옵션}' 3세트 들어옴.
    점수는 0~10. 총 점수를 반환하라.
    """
    bonus2exp = {'S': 1, 'D': 2, 'T': 3}
    points = [0] * 3
    cur_point = 0
    for c in dartResult:
        if c.isdigit():
            cur_point = cur_point * 10 + int(c)
        elif c in bonus2exp:
            points.append(cur_point ** bonus2exp[c])
            cur_point = 0
        elif c == '*':
            points[-2:] = [x * 2 for x in points[-2:]]
        elif c == '#':
            points[-1] *= -1
    return sum(points)



inputdatas = [
    {"data": ["1S2D*3T"], "answer": 37},
    {"data": ["1D2S#10S"], "answer": 9},
    {"data": ["1D2S0T"], "answer": 3},
    {"data": ["1S*2T*3S"], "answer": 23},
    {"data": ["1D#2S*3S"], "answer": 5},
    {"data": ["1T2D3D#"], "answer": -4},
    {"data": ["1D2S3T*"], "answer": 59}
]


"""
2018 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 28,564명, 정답률 59%
예전에는 각 order를 분리한 후에 처리하려고 했었고, 그게 까다로웠다.
개발적으로 생각하면 책임 분리와 확장성을 고려해서 그게 맞는 것 같긴 한데,
여기선 그냥 한글자씩 순회하면서 바로 처리해도 된다.
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
