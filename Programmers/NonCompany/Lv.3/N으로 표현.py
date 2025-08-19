# https://school.programmers.co.kr/learn/courses/30/lessons/42895
"""
constraints:
  • N은 1 이상 9 이하입니다.
  • number는 1 이상 32,000 이하입니다.
  • 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
  • 최솟값이 8보다 크면 -1을 return 합니다.
"""


def solution(N, number):
    dp = [set() for _ in range(9)]
    for cnt in range(1, 9):
        cur_cases = dp[cnt]
        cur_cases.add(int(str(N) * cnt))
        for j in range(1, cnt // 2 + 1):
            for a in dp[j]:
                for b in dp[cnt - j]:
                    cur_cases.update({
                        a + b, a - b, b - a, a * b,
                        *([] if b == 0 else [a // b]),
                        *([] if a == 0 else [b // a])
                    })
        if number in cur_cases:
            return cnt
    return -1


inputdatas = [
    {"data": [5, 12], "answer": 4},
    {"data": [2, 11], "answer": 3}
]

"""
동적계획법(Dynamic Programming)
Lv.3. 현 시점 완료한 사람 18,446명, 정답률 29%
dp는 항상 어렵다.
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
