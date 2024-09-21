# https://school.programmers.co.kr/learn/courses/30/lessons/178871
"""
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부름.
현재 순위대로 이름이 담긴 리스트, 해설진이 부른 순서대로 이름이 담긴 리스트가 주어질 때,
경주가 끝났을 때 선수들의 이름을 순위대로 배열에 담아 반환하라.
5 ≤ players의 길이 ≤ 50,000
2 ≤ callings의 길이 ≤ 1,000,000
"""


def solution(players, callings):
    r2p = {i: p for i, p in enumerate(players)}
    p2r = {p: i for i, p in enumerate(players)}
    for cur_p in callings:
        cur_r = p2r[cur_p]
        prev_p = r2p[cur_r - 1]
        r2p[cur_r - 1], r2p[cur_r] = cur_p, prev_p
        p2r[cur_p] -= 1
        p2r[prev_p] += 1
    return list(r2p.values())




inputdatas = [
    {"data": [["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]], "answer": ["mumu", "kai", "mine", "soe", "poe"]},
]

"""
연습문제
Lv.1. 현 시점 완료한 사람 19,904명, 정답률 45%
다른 사람들은 딕셔너리 하나로 사용하고 리스트에서 직접 스왑했다.
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
