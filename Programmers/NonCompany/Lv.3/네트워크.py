# https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
constraints:
  • 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
  • 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
  • i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
  • computer[i][i]는 항상 1입니다.
"""


def solution(n, computers):
    def dfs(cur):
        visited[cur] = 1
        for nxt in range(n):
            if cur != nxt and not visited[nxt] and computers[cur][nxt]:
                dfs(nxt)
    visited = [0] * n
    network = 0
    for i in range(n):
        if not visited[i]:
            network += 1
            dfs(i)
    return network


inputdatas = [
    {"data": [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "answer": 2},
    {"data": [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], "answer": 1}
]


"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.3. 현 시점 완료한 사람 49,040명, 정답률 63%
기본적 dfs. dfs 푼지 몇년 된 것 같은데 쉬워서 5분만에 풀었다. Lv.1~2로 내려가야 할 것 같음.
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
