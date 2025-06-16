# https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
constraints:

"""
from collections import deque

def solution(progresses, speeds):
    q = deque()
    answer = []
    for p, s in zip(progresses, speeds):
        q.append((p, s))
    while q:
        cnt = 0
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
            continue
        for i in range(len(q)):
            p, s = q[i]
            q[i] = (p + s, s)
    return answer


inputdatas = [
    {"data": [[93, 30, 55], [1, 30, 5]], "answer": [2, 1]},
    {"data": [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]], "answer": [1, 3, 2]}
]


"""
스택/큐
Lv.2. 현 시점 완료한 사람 71,446명, 정답률 66%
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
