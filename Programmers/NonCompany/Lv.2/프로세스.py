# https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""
constraints:
  • priorities의 길이는 1 이상 100 이하입니다.
    ◦ priorities의 원소는 1 이상 9 이하의 정수입니다.
    ◦ priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
  • location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
    ◦ priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
"""
from collections import deque

def solution(priorities, location):
    queue = deque((idx, priority) for idx, priority in enumerate(priorities))
    cnt = 1
    while queue:
        idx, priority = queue.popleft()
        if any(priority < q[1] for q in queue):
            queue.append((idx, priority))
        else:
            if idx == location:
                return cnt
            cnt += 1


inputdatas = [
    {"data": [[2, 1, 3, 2], 2], "answer": 1},
    {"data": [[1, 1, 9, 1, 1, 1], 0], "answer": 5}
]

"""
스택/큐
Lv.2. 현 시점 완료한 사람 58,883명, 정답률 65%
처음에 제한사항의 '숫자가 클 수록 우선순위가 높습니다.'를 못봐서
프로세스 로직과 예시를 이해하지 못해서 잠시 헤맸다.
O(n^2)풀이긴 한데 priorities 길이가 최대 100이라 별 상관없다.
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
