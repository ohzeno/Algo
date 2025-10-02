# https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
constraints:

"""


def solution(phone_book):
    log = set()
    for phone in sorted(phone_book):
        for i in range(1, len(phone)+1):
            if phone[:i] in log:
                return False
        log.add(phone)
    return True


inputdatas = [
    {"data": [["119", "97674223", "1195524421"]], "answer": False},
    {"data": [["123","456","789"]], "answer": True},
    {"data": [["12","123","1235","567","88"]], "answer": False},
    {"data": [["1124", "113", "112"]], "answer": False},
]


"""
해시
Lv.2. 현 시점 완료한 사람 73,154명, 정답률 65%
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
