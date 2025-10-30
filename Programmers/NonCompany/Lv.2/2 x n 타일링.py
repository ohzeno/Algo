# https://school.programmers.co.kr/learn/courses/30/lessons/12900?language=python3
"""
constraints:
  • 가로의 길이 n은 60,000이하의 자연수 입니다.
  • 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.
"""


def solution(n):
    MOD = int(1e9+7)
    dp = [0] * (n+1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]


inputdatas = [
    {"data": [4], "answer": 5}
]


"""
연습문제
Lv.2. 현 시점 완료한 사람 16,326명, 정답률 59%
타일링 오랜만에 보니 풀이가 기억나지 않았다.
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
