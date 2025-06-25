# https://school.programmers.co.kr/learn/courses/30/lessons/43238
"""
constraints:
  • 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
  • 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
  • 심사관은 1명 이상 100,000명 이하입니다.
"""


def solution(n, times):
    ll, rr = 1, max(times) * n
    while ll < rr:
        mid = (ll + rr) // 2
        if sum(mid // t for t in times) < n:
            ll = mid + 1
        else:
            rr = mid
    return ll


inputdatas = [
    {"data": [6, [7, 10]], "answer": 28}
]


"""
이분탐색
Lv.3. 현 시점 완료한 사람 23,924명, 정답률 47%
이분 탐색 경계값들도 항상 어렵다. 아직도 명확한 설명을 본 적이 없다.
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
