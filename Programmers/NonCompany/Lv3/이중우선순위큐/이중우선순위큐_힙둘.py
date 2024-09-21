# https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""
이중 우선순위 큐는 다음 연산을 할 수 있는 구조를 말한다.
I 숫자: 큐에 주어진 숫자를 삽입
D 1: 큐에서 최댓값을 삭제
D -1: 큐에서 최솟값을 삭제
opetations가 주어지면 모든 연산을 처리한 후
큐가 비어있으면 [0, 0], 비어있지 않으면 [최댓값, 최솟값]을 반환하라.
- 1 <= len(operations) <= 1,000,000
삭제 연산에서 최대, 최소값이 둘 이상이면 하나만 삭제
빈 큐에 삭제 연산이 주어지면 무시
"""
from heapq import heappush as hpush, heappop as hpop


def remove_item(heap, item):
    idx = heap.index(-item)
    heap[idx] = heap[-1]
    heap.pop()


def solution(operations):
    max_h, min_h = [], []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == "I":
            hpush(max_h, -int(num))
            hpush(min_h, int(num))
        elif max_h:
            if num == "1":
                remove_item(min_h, hpop(max_h))
            else:
                remove_item(max_h, hpop(min_h))
    return [-max_h[0], min_h[0]] if max_h else [0, 0]


inputdatas = [
    {
        "data": [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]],
        "answer": [0, 0],
    },
    {
        "data": [
            ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
        ],
        "answer": [333, -45],
    },
]

"""
힙(Heap).
Lv.3. 현 시점 완료한 사람 24,544명, 정답률 61%
일단 최대힙, 최소힙으로 구현해봤다.
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
