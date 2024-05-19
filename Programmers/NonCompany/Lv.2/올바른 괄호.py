# https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""
1~n까지 번호가 붙어있는 n명의 사람이 순서대로 단어를 말한다.
앞 사람의 단어 마지막 문자로 시작하는 단어를 말해야 한다.
중복은 불가하고 두 글자 이상이어야 한다.
사람 수 n과 사람들이 말한 단어 목록 words가 주어질 때,
가장 먼저 탈락하는 사람 번호와, 그 사람이 자신의 몇 번째 차례에 탈락하는지를 반환하라.
탈락자가 없다면 [0, 0]을 반환한다.
"""


def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True


inputdatas = [
    {
        "data": ["()()"],
        "answer": True,
    },
    {
        "data": ["(())()"],
        "answer": True,
    },
    {
        "data": [")()("],
        "answer": False,
    },
    {
        "data": ["(()("],
        "answer": False,
    },
]

"""
Lv.2. 현 시점 완료한 사람 46,953명, 정답률 78%
초보적인 괄호 유효성 검사 문제. 솔직히 이게 lv.0~1이 아닌 이유를 모르겠다.
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
