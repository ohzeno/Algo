# https://school.programmers.co.kr/learn/courses/30/lessons/340199
"""
constraints:
  • wallet의 길이 = bill의 길이 = 2
  • 10 ≤ wallet[0], wallet[1] ≤ 100
  • 10 ≤ bill[0], bill[1] ≤ 2,000
"""


def solution(wallet, bill):
    fold = 0
    wallet.sort()
    bill.sort()
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[1] //= 2
        bill.sort()
        fold += 1
    return fold


inputdatas = [
    {"data": [[30, 15], [26, 17]], "answer": 1},
    {"data": [[50, 50], [100, 241]], "answer": 4}
]


"""
PCCE 기출문제
Lv.1. 현 시점 완료한 사람 411명, 정답률 59%
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
