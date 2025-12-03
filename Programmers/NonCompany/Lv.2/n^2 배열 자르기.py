# https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""
constraints:
  • 1 ≤ n ≤ 10^7
  • 0 ≤ left ≤ right < n^2
  • right - left < 10^5
"""


def solution(n, left, right):
    ans = []
    for i in range(left, right + 1):
        r, c = divmod(i, n)
        ans.append(max(r, c) + 1)
    return ans


inputdatas = [
    {"data": [3, 2, 5], "answer": [3,2,2,3]},
    {"data": [4, 7, 14], "answer": [4,3,3,3,4,4,4,4]},
    {"data": [3, 3, 4], "answer": [2, 2]},
]


"""
월간 코드 챌린지 시즌3
Lv.2. 현 시점 완료한 사람 18,100명, 정답률 68%
n이 10^7이라 2차원 배열은 8*10^14 byte = 800 TB 메모리 초과.
2중 for문에 r*n+c가 left, right 사이인지 확인해서 넣으면 시간 초과.
결국 left에서 right까지 순회하면서 넣어야 함.
정답률이 높은 이유는 복붙 때문. Lv.2라기엔 제한사항이 까다롭고 최적화도 어려운 문제.
문제에서 제시한 알고리즘을 그대로 구현하고 3번 최적화해도 시간 초과가 났다.
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
