# https://school.programmers.co.kr/learn/courses/15009/lessons/121689
"""
카페에 0초에 손님이 도착. 이후 k초마다 손님이 도착.
주문받은 순서대로 음료 만듦. 주문한 음료 받은 손님은 바로 나감.
각 음료 제조시간과 손님들의 주문 음료 순서, 방문간격이 주어질 때,
카페에 동시에 존재한 손님 수 최대값 리턴하라.

1 ≤ len(menu) ≤ 100
    1 ≤ menu[i] ≤ 100
1 ≤ len(order) ≤ 10,000
    0 ≤ order[i] < menu의 길이
1 ≤ k ≤ 100
"""
from collections import deque


def solution(menu, order, k):
    max_c = 1
    enters = deque([i * k for i in range(len(order))])
    q = deque([enters.popleft()])
    t = 0
    for i, o in enumerate(order):
        # 현재 주문 음료 제작 완료 시각
        # max(이전 주문 완료 시각, 현재 손님 입장 시각) + 주문 음료 제작 시간
        t = max(t, i * k) + menu[o]
        while enters and enters[0] < t:  # 제작 완료 직전까지 손님 누적
            q.append(enters.popleft())
        max_c = max(max_c, len(q))  # 최대 손님 수 갱신
        q.popleft()  # 현재 주문 손님 제거
        # 완료 시각에 도착한 손님 추가
        # (나가는 손님이 먼저 퇴장한 다음 들어오는 손님이 입장합니다.)
        if enters and enters[0] == t:
            q.append(enters.popleft())
    return max_c


inputdatas = [
    [[[5, 12, 30], [1, 2, 0, 1], 10], 3],
    [[[5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10], 4],
    [[[5], [0, 0, 0, 0, 0], 5], 1],
]

"""
[PCCP 모의고사 #2] 3번 - 카페 확장
레벨1~2, 실~골5, ps 좀 해봤으면 웰노운이라 쉽다는 댓글들이 있다.
ps 700문제 가량 풀었고 플레, 다이아, 레벨4도 많이 풀었고, 
실제 코테들에서 내가 꾸준히 최상위권인데 쉽지 않았다.
내가 단순히 이 유형에 익숙하지 않을 수도 있지만 
700문제 풀고 익숙치 않은 문제를 웰노운이라고 할 수 있나...?
"""

for data, ans in inputdatas:
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
