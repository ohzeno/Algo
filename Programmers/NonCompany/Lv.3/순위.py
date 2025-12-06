# https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""
constraints:
  • 선수의 수는 1명 이상 100명 이하입니다.
  • 경기 결과는 1개 이상 4,500개 이하입니다.
  • results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
  • 모든 경기 결과에는 모순이 없습니다.
"""


def solution(n, results):
    # win[i][j] = 1이면 i가 j를 이김. -1이면 i가 j에게 패배. 0이면 모름
    win_lose = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        win_lose[a][b] = 1
        win_lose[b][a] = -1

    for mid in range(1, n + 1):
        for st in range(1, n + 1):
            for ed in range(1, n + 1):
                if win_lose[st][mid] and win_lose[st][mid] == win_lose[mid][ed]:
                    win_lose[st][ed] = win_lose[st][mid]
                    win_lose[ed][st] = -win_lose[st][mid]

    confirmed = 0
    for a in range(1, n + 1):
        cnt = 0
        # a와 승패가 결정된 선수 수
        for b in range(1, n + 1):
            if win_lose[a][b] != 0:
                cnt += 1
        if cnt == n - 1:
            confirmed += 1
    return confirmed


inputdatas = [
    {"data": [5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]], "answer": 2}
]


"""
그래프
Lv.3. 현 시점 완료한 사람 14,220명, 정답률 43%
플로이드-워셜 응용. 정답률 거품인듯.
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
