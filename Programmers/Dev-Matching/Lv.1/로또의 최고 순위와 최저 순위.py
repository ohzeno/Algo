# https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""
constraints:
  • lottos는 길이 6인 정수 배열입니다.
  • lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
    ◦ 0은 알아볼 수 없는 숫자를 의미합니다.
    ◦ 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
    ◦ lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
  • win_nums은 길이 6인 정수 배열입니다.
  • win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
    ◦ win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
    ◦ win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
"""


def solution(lottos, win_nums):
    matches = len(set(lottos) & set(win_nums))
    ans = [matches + lottos.count(0), matches]
    for i, case in enumerate(ans):
        ans[i] = 6 if case < 2 else 7 - case
    return ans


inputdatas = [
    {"data": [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]], "answer": [3, 5]},
    {"data": [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]], "answer": [1, 6]},
    {"data": [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]], "answer": [1, 1]}
]


"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기)
Lv.1. 현 시점 완료한 사람 45,743명, 정답률 59%
이전에 풀 때는 40290명, 57%였다.
이번엔 문제 읽고 풀이 작성, 개선까지 5분 걸렸다.
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
