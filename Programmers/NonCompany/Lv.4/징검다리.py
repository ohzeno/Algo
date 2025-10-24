# https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""
constraints:
  • 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
  • 바위는 1개 이상 50,000개 이하가 있습니다.
  • n 은 1 이상 바위의 개수 이하입니다.
"""


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    ll, rr = 0, distance
    max_of_min = None
    while ll <= rr:
        mid = (ll + rr) // 2
        prev = deleted = 0
        for rock in rocks:
            if rock - prev < mid:
                deleted += 1
                if deleted > n:
                    break
            else:
                prev = rock
        if deleted > n:
            rr = mid - 1
        else:
            max_of_min = mid
            ll = mid + 1
    return max_of_min


inputdatas = [
    {"data": [25, [2, 14, 11, 21, 17], 2], "answer": 4}
]


"""
이분탐색
Lv.4. 현 시점 완료한 사람 8,203명, 정답률 29%
백준에선 실버 1이었는데 여긴 Lv.4인게 유머.
복붙할 블로그 풀이가 적어서 그런 듯.
Lv.3쯤이라고 생각한다. 징검다리를 접해보지 않았으면 어려운 문제.
이분탐색은 항상 경계조건, 무엇을 반환할지, 조건 만족시 어느 포인터를 이동할지 등이 어렵다.
'탐색이 끝났을 때 뭘 남길 것인가'를 위주로 생각하면 좋다. 
여기선 rr을 반환해도 되지만 매번 ll, rr 어느쪽을 반환할지 생각하는게 어려우니
따로 max_of_min 처럼 조건 만족한 포인터를 저장해두는게 직관적이다.
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
