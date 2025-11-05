# https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""
constraints:

"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 위에서 bridge_length초?
    bridge = deque()
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    absolute_t = 0
    while bridge or truck_weights:
        if bridge and bridge[0][1] == bridge_length:
            truck_weight, t = bridge.popleft()
            bridge_weight -= truck_weight
        if truck_weights and bridge_weight + truck_weights[0] <= weight and len(bridge) < bridge_length:
            truck_weight = truck_weights.popleft()
            bridge.append([truck_weight, 0])
            bridge_weight += truck_weight
        absolute_t += 1
        for truck in bridge:
            truck[1] += 1
    return absolute_t


inputdatas = [
    {"data": [2, 10, [7,4,5,6]], "answer": 8},
    {"data": [100, 100, [10]], "answer": 101},
    {"data": [100, 100, [10,10,10,10,10,10,10,10,10,10]], "answer": 110}
]


"""
스택/큐
Lv.2. 현 시점 완료한 사람 45,559명, 정답률 55%
다리를 지나는 데 걸리는 시간을 지문에서 명시 안해놨다.
예시들을 검토하며 추론해야 한다.
처음에 차량이 시간당 1씩 움직인다는걸 몰라서 while로 시간 달성하면 다 빼줬었다.

다른 풀이는 시간을 추적하지 않고 0을 넣어서 시간과 길이 제한을 함께 처리했다.
좋은 방법이지만 코테 현장에서 떠올리기엔 특이한 방식인듯.
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
