# https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""
constraints:
  • 전체 학생의 수는 2명 이상 30명 이하입니다.
  • 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
  • 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
  • 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
  • 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
"""


def solution(n, lost, reserve):
    l_set, r_set = set(lost), set(reserve)
    lost = sorted(l_set - r_set)
    reserve = sorted(r_set - l_set)
    lost_cnt = len(lost)
    for l in lost:
        for r in reserve:
            if l - 1 <= r <= l + 1:
                reserve.remove(r)
                lost_cnt -= 1
                break
    return n - lost_cnt


inputdatas = [
    {"data": [5, [2, 4], [1, 3, 5]], "answer": 5},
    {"data": [5, [2, 4], [3]], "answer": 4},
    {"data": [3, [3], [1]], "answer": 2},
    {"data": [5, [1, 3, 4], [1, 2, 3]], "answer": 4},
]


"""
탐욕법(Greedy)
Lv.1. 현 시점 완료한 사람 61,649명, 정답률 58%

여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

여벌 갖고온 학생이 도난당했을 경우 다른 학생에게 빌려줄 수 없다는 조건을 못봐서 잠깐 헤맸다.
정답률 58%도 그렇고 함정과 방법론을 보면 lv.1이라고 판정한 이유를 잘 모르겠다.
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
