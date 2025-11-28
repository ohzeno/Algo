# https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""
constraints:

"""


def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)


inputdatas = [
    {"data": ["1924", 2], "answer": "94"},
    {"data": ["1231234", 3], "answer": "3234"},
    {"data": ["4177252841", 4], "answer": "775841"}
]


"""
탐욕법(Greedy)
Lv.2. 현 시점 완료한 사람 32,672명, 정답률 55%
원본 릿코드 문제가 정답률 33%인데 여긴 55%에 Lv.2다.
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
