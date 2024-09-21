# https://school.programmers.co.kr/learn/courses/30/lessons/120843
"""
constraints:
  • 2 < numbers의 길이 < 100
  • 0 < k < 1,000
  • numbers의 첫 번째와 마지막 번호는 실제로 바로 옆에 있습니다.
  • numbers는 1부터 시작하며 번호는 순서대로 올라갑니다.
"""


def solution(numbers, k):
    return numbers[(k-1) * 2 % len(numbers)]


inputdatas = [
    {"data": [[1, 2, 3, 4], 2], "answer": 3},
    {"data": [[1, 2, 3, 4, 5, 6], 5], "answer": 3},
    {"data": [[1, 2, 3], 3], "answer": 2}
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 16,514명, 정답률 82%
간단한 인덱싱, 나머지 연산 문제.
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
