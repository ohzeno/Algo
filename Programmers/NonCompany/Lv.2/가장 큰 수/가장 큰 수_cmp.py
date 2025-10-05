# https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""
constraints:

"""


from functools import cmp_to_key
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))
    return str(int(''.join(numbers)))


inputdatas = [
    {"data": [[6, 10, 2]], "answer": "6210"},
    {"data": [[3, 30, 34, 5, 9]], "answer": "9534330"},
    {"data": [[1, 10, 100, 1000]], "answer": "1101001000"},
    {"data": [[0, 0, 0] ], "answer": "0"},
]


"""
정렬
Lv.2. 현 시점 완료한 사람 57,912명, 정답률 56%
비슷한 문제를 옛날에 풀었던 것도 같긴 한데 Lv.2에 있을 문제는 아니다.
릿코드 원본 문제가 Medium이고 정답률 41.8%인걸 생각하면
정답률은 블로그 풀이 복붙때문에 높은 것이 확실.

cmp_to_key로 더 직관적으로 바꿔봤다.
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
