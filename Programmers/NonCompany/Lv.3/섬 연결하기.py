# https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""
constraints:

"""


def solution(n, costs):
    def find_p(x):
        if p[x] != x:
            p[x] = find_p(p[x])  # 부모 갱신
        return p[x]
    def union(x, y):
        nx, ny = find_p(x), find_p(y)
        if nx != ny:
            p[max(nx, ny)] = min(nx, ny)
    p = [i for i in range(n + 1)]
    costs.sort(key=lambda x: x[2])
    edges_used = 0
    tot_cost = 0
    for a, b, cost in costs:
        if find_p(a) != find_p(b):
            union(a, b)
            tot_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                return tot_cost
    return tot_cost


inputdatas = [
    {"data": [4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]], "answer": 4}
]


"""
탐욕법(Greedy)
Lv.3. 현 시점 완료한 사람 17,567명, 정답률 49%
그리디-크루스칼이다.
최소신장트리를 풀어본지 몇년 돼서 완전히 잊고 헤맸다.
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
