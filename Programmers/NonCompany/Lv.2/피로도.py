# https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
constraints:
  • k는 1 이상 5,000 이하인 자연수입니다.
  • dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
    ◦ dungeons의 가로(열) 길이는 2 입니다.
    ◦ dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
    ◦ "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
    ◦ "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
    ◦ 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
"""


def solution(k, dungeons):
    def dfs(fatigue, explored_cnt):
        nonlocal max_explored
        max_explored = max(max_explored, explored_cnt)
        for i in range(n):
            if visited[i]:
                continue
            min_required_fatigue, cost = dungeons[i]
            if fatigue >= min_required_fatigue:
                visited[i] = True
                dfs(fatigue - cost, explored_cnt + 1)
                visited[i] = False
    n = len(dungeons)
    visited = [False] * n
    max_explored = 0
    dfs(k, 0)
    return max_explored


inputdatas = [
    {"data": [80, [[80,20],[50,40],[30,10]]], "answer": 3}
]


"""
완전탐색
Lv.2. 현 시점 완료한 사람 29,565명, 정답률 67%
완탐으로 분류돼있는데 dfs로 보여서 잠시 혼란스러웠다.
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
