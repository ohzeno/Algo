# https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""
constraints:
  • 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
  • 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
"""


def solution(citations):
    # 이분탐색? 하지만 파라미터 범위가 좁다.
    # 브루트포스?
    # 이상과 이하가 같이 있어서 경계 애매.
    # 위키 확인 결과 '이하'는 조건에 없음. 문제 출제자가 잘못된 조건을 추가한 듯
    # 정렬 탐색 -> nlogn + n
    # 이분탐색 -> nlogn + n(rr을 max로 사용하면)
    ll, rr = 0, 10000
    succeeded = 0
    while ll <= rr:
        mid = (ll + rr) // 2
        cnt = 0
        for citation in citations:
            if citation >= mid:
                cnt += 1
        if cnt >= mid:
            succeeded = mid
            ll = mid + 1
        else:
            rr = mid - 1
    return succeeded


inputdatas = [
    {"data": [[3, 0, 6, 1, 5]], "answer": 3},
    {"data": [[10, 8, 5, 4, 3]], "answer": 4},
    {"data": [[25, 8, 5, 3, 3]], "answer": 3},
    {"data": [[5, 5, 5]], "answer": 3},
    {"data": [[0]], "answer": 0},
    {"data": [[3, 4]], "answer": 2},
    {"data": [[1, 2, 3, 5, 6, 7, 10, 11]], "answer": 5},
    {"data": [[3, 5, 11, 6, 1, 5, 3, 3, 1, 41]], "answer": 5},
    {"data": [[1, 11, 111, 1111]], "answer": 3},
]


"""
정렬
Lv.2. 현 시점 완료한 사람 55,394명, 정답률 67%
다른 풀이들은 증명이 아닌 말들을 증명이라고 주장하고 설명과 다른 코드를 사용했다.
다른 풀이들은 비직관적이고 증명을 따로 하기도 귀찮아서 내 풀이를 고치진 않았다.
처음 보자마자 떠오른대로 이분탐색으로도 풀어봤다.
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
