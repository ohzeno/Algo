# https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""
한 번에 1 or 2칸 이동 가능.
칸 수가 주어질 때 끝에 도달하는 방법을 1234567로 나눈 나머지 리턴.
n은 1 이상 2000 이하 정수.
"""


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0, 1, 2] + [0] * (n - 2)
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]


inputdatas = [
    {"data": [4], "answer": 5},
    {"data": [3], "answer": 3},
]

"""
연습문제
Lv.2. 현 시점 완료한 사람 21,016명, 정답률 69%
단순한 dp 문제.
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
