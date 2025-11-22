# https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""
constraints:
  • prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
  • prices의 길이는 2 이상 100,000 이하입니다.
"""


def solution(prices):
    stack = []
    ans = [0] * len(prices)
    for t, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            tmp_t, tmp_price = stack.pop()
            ans[tmp_t] = t - tmp_t
        stack.append([t, price])
    while stack:
        tmp_t, tmp_price = stack.pop()
        ans[tmp_t] = t - tmp_t
    return ans


inputdatas = [
    {"data": [[1, 2, 3, 2, 3]], "answer": [4, 3, 1, 1, 0]}
]


"""
스택/큐
Lv.2. 현 시점 완료한 사람 51,031명, 정답률 62%
스택을 사용한다는 아이디어 떠올리는데 시간이 조금 걸렸다.
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
