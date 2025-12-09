# https://school.programmers.co.kr/learn/courses/30/lessons/12927
"""
constraints:

"""
import heapq
from heapq import heappush, heappop, heapify

def solution(n, works):
    if n >= sum(works):
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        max_work = heappop(works)
        heappush(works, max_work + 1)
    return sum(w ** 2 for w in works)


inputdatas = [
    {"data": [4, [4, 3, 3]], "answer": 12},
    {"data": [1, [2, 1, 2]], "answer": 6},
    {"data": [3, [1,1]], "answer": 0},
    {"data": [7, [10, 5, 7]], "answer": 75},
    {"data": [999, [800, 100, 55, 45]], "answer": 1},
]


"""
연습문제
Lv.3. 현 시점 완료한 사람 14,539명, 정답률 62%
divmod 써보려 했는데, 몫과 나머지가 일관되게 적용되는게 아니라서 결국 매번 최댓값을 찾아줘야 한다.
work값이 크다고 다 빼버려도 안되고 rem이 크다고 다 빼버려도 안된다.
제곱수의 합이기에 전체가 골고루 작아져야 한다.
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
