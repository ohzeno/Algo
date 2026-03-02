# https://school.programmers.co.kr/learn/courses/30/lessons/12938
"""
constraints:
  • 최고의 집합은 로 return 해주세요.
  • 만약 최고의 집합이 존재하지 않는 경우에 에 -1 을 채워서 return 해주세요.
  • 자연수의 개수 n은 1 이상 10,000 이하의 자연수입니다.
  • 모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수입니다.
"""


def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n] * n
    for i in range(1, s % n + 1):
        answer[-i] += 1
    return answer


inputdatas = [
    {"data": [2, 9], "answer": [4, 5]},
    {"data": [2, 1], "answer": [-1]},
    {"data": [2, 8], "answer": [4, 4]}
]


"""
연습문제
Lv.3. 현 시점 완료한 사람 14,379명, 정답률 58%
예시를 보고 생각한 것은 곱의 크기는 1, 8보다 4, 5처럼 가운데에 가까울 때 클 것 같다는 것.
직관이었고 몇가지 검증을 거쳤다. S의 값을 바꿔가며 생각해봐도 모두 가설대로의 결과가 나왔다.
원소 갯수가 임의면 여러 케이스를 검증해봐야 해서 더 복잡했겠지만 다행히 n이 주어졌다.
첫 아이디어로 구현 후 제출하니 정답.
항상 그렇듯 당연히 증명이 있는 블로그는 못찾아서 직접 증명도 해봤는데,
대우교환 논증 귀류법 혹은 2차방정식을 이용해 2항에 대해 증명 후 n항으로 확장할 수 있다.
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
