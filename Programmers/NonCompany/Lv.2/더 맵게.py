# https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""
constraints:

"""
from heapq import heappush, heappop

def solution(scoville, K):
    # 섞은 음식 지수 = 가장 맵지 않은 음식 지수 + (두 번째로 맵지 않은 음식 지수 * 2)
    # 모든 음식 k 이상 될 때까지 반복하여 섞음.
    # 최소 섞는 횟수?
    answer = 0
    heap = []
    for s in scoville:
        heappush(heap, s)
    while heap:
        first = heappop(heap)
        if first >= K:
            break
        if not heap:
            return -1
        second = heappop(heap)
        new_scoville = first + (second * 2)
        heappush(heap, new_scoville)
        answer += 1
    return answer


inputdatas = [
    {"data": [[1, 2, 3, 9, 10, 12], 7], "answer": 2}
]


"""
힙(Heap)
Lv.2. 현 시점 완료한 사람 47,220명, 정답률 61%
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
