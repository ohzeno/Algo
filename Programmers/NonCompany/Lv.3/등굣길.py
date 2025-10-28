# https://school.programmers.co.kr/learn/courses/30/lessons/42898
"""
constraints:
  • 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
    ◦ m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
  • 물에 잠긴 지역은 0개 이상 10개 이하입니다.
  • 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
"""


def solution(m, n, puddles):
    MOD = int(1e9+7)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for c, r in puddles:
        dp[r][c] = -1
    dp[1][1] = 1
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if dp[r][c] == -1:
                dp[r][c] = 0
                continue
            dp[r][c] += (dp[r-1][c] + dp[r][c-1]) % MOD
    return dp[n][m]


inputdatas = [
    {"data": [4, 3, [[2, 2]]], "answer": 4},
]


"""
동적계획법(Dynamic Programming)
Lv.3. 현 시점 완료한 사람 22,495명, 정답률 61%
좌표계 함정이 악의적이다. m,n인데 m이 col, n이 row임
dp[r][c] = 0를 하지 않아도 되지만 그럼 매번 (r-1, c), (r, c-1)가 -1이 아닌지 확인해야함.

처음에 dfs로 풀었는데, '오른쪽과 아래쪽으로만 움직여' 갈 수 있다는 조건을 못봤기 때문이다.
그 조건이 없으면 {"data": [5, 3, [[2, 1], [2, 2], [4, 2], [4, 3]]], "answer": 1},
같이 ㄹ자 형태로 움직여야 하고, 그러면 dfs가 필요하다.
이 조건때문에 dp가 가능함.
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
