# https://school.programmers.co.kr/learn/courses/30/lessons/120863
"""
constraints:
  • 0 < polynomial에 있는 수 < 100
  • polynomial에 변수는 'x'만 존재합니다.
  • polynomial은 양의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.
  • 항과 연산기호 사이에는 항상 공백이 존재합니다.
  • 공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.
  • 하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.
  • " + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.
  • 0으로 시작하는 수는 없습니다.
  • 문자와 숫자 사이의 곱하기는 생략합니다.
  • polynomial에는 일차 항과 상수항만 존재합니다.
  • 계수 1은 생략합니다.
  • 결괏값에 상수항은 마지막에 둡니다.
  • 0 < polynomial의 길이 < 50
"""


def solution(polynomial):
    x = constants = 0
    for term in polynomial.split(" + "):
        if term[-1] == "x":
            x += int(term[:-1]) if term[:-1] != "" else 1
        else:
            constants += int(term)
    if x == 0:
        return str(constants)
    elif x == 1:
        return f"x + {constants}" if constants else "x"
    return f"{x}x + {constants}" if constants else f"{x}x"


inputdatas = [
    {"data": ["3x + 7 + x"], "answer": "4x + 7"},
    {"data": ["x + x + x"], "answer": "3x"},
    {"data": ["x"], "answer": "x"},
    {"data": ["7"], "answer": "7"},
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 11,623명, 정답률 72%
레벨 0, 정답률 72%치고는 까다로운 문제.
제약조건에 x의 존재여부, 상수항의 존재여부 설명이 없다.
그렇게 어렵지는 않지만 실수할 부분이 꽤 있어서 lv.1정도로 보인다.
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
