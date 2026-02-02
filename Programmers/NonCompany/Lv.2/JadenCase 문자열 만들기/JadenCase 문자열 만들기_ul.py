# https://school.programmers.co.kr/learn/courses/30/lessons/12951
"""
constraints:

"""


def solution(s):
    ss = s.split(" ")
    res = []
    for word in ss:
        if len(word) == 0:
            res.append(word)
            continue
        nword = word[0].upper() + word[1:].lower()
        res.append(nword)
    return " ".join(res)


inputdatas = [
    {"data": ["3people unFollowed me"], "answer": "3people Unfollowed Me"},
    {"data": ["for the last week"], "answer": "For The Last Week"}
]


"""
연습문제
Lv.2. 현 시점 완료한 사람 44,486명, 정답률 80%
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
