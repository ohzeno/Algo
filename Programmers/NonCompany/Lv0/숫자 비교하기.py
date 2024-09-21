# https://school.programmers.co.kr/learn/courses/30/lessons/120807
"""
같으면 1, 다르면 -1 반환
"""
def solution(num1, num2):
    return 1 if num1 == num2 else -1


inputdatas = [
    {"data": [2, 3], "answer": -1},
    {"data": [11, 11], "answer": 1},
    {"data": [7, 99], "answer": -1},
]

"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 68,649명, 정답률 91%
옛날에 풀었으면 early return 사용했을듯
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
