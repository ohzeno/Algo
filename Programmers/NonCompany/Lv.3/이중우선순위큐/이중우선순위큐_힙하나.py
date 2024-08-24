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
from heapq import heappush, heappop


def solution(operations):
    heap = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == "I":
            heappush(heap, int(num))
        elif heap:
            if num == "1":
                heap.remove(max(heap))
            else:
                heappop(heap)
    return [max(heap), heap[0]] if heap else [0, 0]


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
최대값 찾을 때 max로 찾기 때문에 제거 후 heapify를 하지 않아도 된다. 
비슷한 풀이가 있어 댓글들을 훑어보니
최대값 제거 후 heap구조 깨진다고 틀린 풀이라는 사람들이 가득한데...
사람들이 코드를 읽고있는게 맞는지 의심스럽다.

뒷부분 구조가 깨지든 말든 최대값은 max로 찾아서 상관없고,
최소값은 루트에 위치하고 있고, 
최대값 제거하려다 루트를 제거하는 경우는 원소가 하나 뿐일 때라 상관없다.

그래서 heap 하나로 구현 가능하다.
max가 O(n)이므로 시간효율성은 안좋다.
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
