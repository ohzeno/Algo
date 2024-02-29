# https://school.programmers.co.kr/learn/courses/15009/lessons/121688
"""
신입교육 한 번에 2인 교육.
각 능력치가 1, 3이면 교육 후에는 각각 둘의 이전 능력치의 합이 되어 4, 4가 된다.
민수는 산업스파이이므로 모든 신입사원 능력 합을 최소화하고 싶다.
교육 후 능력치 합의 최솟값을 리턴하라.
2 ≤ len(ability) ≤ 1,000
1 ≤ ability[i] ≤ 1,000
1 ≤ number ≤ 1,000
"""
from heapq import heappop as hpop, heappush as hpush, heapify
def solution(ability, number):
    heapify(ability)
    for _ in range(number):
        new = hpop(ability) + hpop(ability)
        hpush(ability, new)
        hpush(ability, new)
    return sum(ability)

inputdatas = [
    [[[10, 3, 7, 2], 2], 37],
    [[[1, 2, 3, 4], 3], 26],
]

"""
[PCCP 모의고사 #2] 2번 - 신입사원 교육
sort를 사용하면 시간초과.
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")