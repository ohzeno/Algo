# https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
우선순위 디스크 컨트롤러
1. 요청 들어오면 [번호, 요청 시각, 소요시간] 저장해두는 대기 큐
2. 하드가 작업 안하고 대기 큐가 비어있지 않으면 우선순위 높은 작업 꺼내서 실행.
    [소요시간, 요청 시각, 번호]가 작은 순으로 우선순위 높음
3. 하드 작업 끝나는 순간에도 컨트롤러 작동함
반환시간: 종료-요청시각
모든 요청 작업의 반환 시간의 평균의 정수부분을 return
jobs: [요청 시각, 소요시각]
constraints:
"""
from heapq import heappush, heappop
from collections import deque
def solution(jobs):
    heap = []
    jobs = deque(sorted(jobs, key=lambda x: x[0]))
    cur_t = job_idx = 0
    turnaround_ts = []
    while jobs or heap:
        while jobs and jobs[0][0] <= cur_t:
            req_t, cost = jobs.popleft()
            heappush(heap, (cost, req_t, job_idx))
            job_idx += 1
        if heap:
            cost, req_t, idx = heappop(heap)
            cur_t += cost
            turnaround_ts.append(cur_t - req_t)
        else:
            cur_t = jobs[0][0]
    return sum(turnaround_ts) // len(turnaround_ts)


inputdatas = [
    {"data": [[[0, 3], [1, 9], [3, 5]]], "answer": 8},
    {"data": [[[0, 3], [0, 5], [0, 2]]], "answer": 5},
]


"""
힙(Heap)
Lv.3. 현 시점 완료한 사람 23,782명, 정답률 46%
공회전을 고려 안해서 첫 풀이는 통과하지 못했다.
다른 풀이들이 간결하나 복붙 풀이들이 항상 그렇듯 수학적 증명 없이 조건을 무시한 풀이들이기에
풀이를 바꾸지 않았다.
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
