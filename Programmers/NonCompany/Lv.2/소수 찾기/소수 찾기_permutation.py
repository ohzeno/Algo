# https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""
constraints:
  • numbers는 길이 1 이상 7 이하인 문자열입니다.
  • numbers는 0~9까지 숫자만으로 이루어져 있습니다.
  • "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
"""
from itertools import permutations

def solution(numbers):
    primes = set()
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    for i in range(1, len(numbers)+1):
        for permutation in permutations(numbers, i):
            num = int("".join(permutation))
            if is_prime(num):
                primes.add(num)
    return len(primes)


inputdatas = [
    {"data": ["17"], "answer": 3},
    {"data": ["011"], "answer": 2}
]


"""
완전탐색
Lv.2. 현 시점 완료한 사람 44,910명, 정답률 56%
순열과 소수판정 결합 문제가 Lv.2에 있을 이유가 없다.
프로그래머스도 solved.ac같이 난이도 기여가 있어야 한다.
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
