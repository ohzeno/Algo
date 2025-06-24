# https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""
constraints:
  • 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
  • 각 숫자는 1 이상 50 이하인 자연수입니다.
  • 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""


def solution(numbers, target):
    def dfs(idx, acc=0):
        nonlocal cnt
        if idx == n:
            if acc == target:
                cnt += 1
            return
        dfs(idx + 1, acc + numbers[idx])
        dfs(idx + 1, acc - numbers[idx])

    n = len(numbers)
    cnt = 0
    dfs(0)
    return cnt


inputdatas = [
    {"data": [[1, 1, 1, 1, 1], 3], "answer": 5},
    {"data": [[4, 1, 2, 1], 4], "answer": 2}
]

"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.2. 현 시점 완료한 사람 64,215명, 정답률 63%
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
