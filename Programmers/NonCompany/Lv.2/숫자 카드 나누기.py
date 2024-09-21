# https://school.programmers.co.kr/learn/courses/30/lessons/135807
"""
둘 중 하나를 만족하는 가장 큰 양의 정수를 구해야 함
1. 철수가 가진 카드의 모든 숫자를 나눌 수 있고,
    영희가 가진 카드의 숫자들 중 하나도 나눌 수 없는 양의 정수
2. 영희가 가진 카드의 모든 숫자를 나눌 수 있고,
    철수가 가진 카드의 숫자들 중 하나도 나눌 수 없는 양의 정수
만족하는 수가 없으면 0을 반환

1 ≤ arrayA의 길이 = arrayB의 길이 ≤ 500,000
1 ≤ arrayA의 원소, arrayB의 원소 ≤ 100,000,000
arrayA와 arrayB에는 중복된 원소가 있을 수 있습니다.
"""
from math import gcd
from functools import reduce

def find_gcd(numbers):
    return reduce(gcd, numbers)

def cannot_divide_any(divisor, array):
    return all(x % divisor != 0 for x in array)

def solution(arrayA, arrayB):
    # gcd_A는 A를 나눌 수 있음.
    gcd_A, gcd_B = map(find_gcd, [arrayA, arrayB])
    ans = 0
    if cannot_divide_any(gcd_A, arrayB):  # A를 나눌 수 있지만 B를 나눌 수 없다면
        ans = max(ans, gcd_A)
    if cannot_divide_any(gcd_B, arrayA):
        ans = max(ans, gcd_B)
    return ans


inputdatas = [
    {"data": [[10, 17], [5, 20]], "answer": 0},
    {"data": [[10, 20], [5, 17]], "answer": 10},
    {"data": [[14, 35, 119], [18, 30, 102]], "answer": 7},
]

"""
연습문제 
Lv.2. 현 시점 완료한 사람 5,067명, 정답률 49%
이게 레벨 2가 맞나...
최대공약수를 이용한다. A의 최대공약수는 A의 원소 전부를 나눌 수 있다.
그 최대공약수가 B를 나눌 수 없다면 조건을 만족하는 것.
물론 99.99%는 그냥 복붙 풀이다.
A의 최대공약수가 아니더라도 A의 원소를 전부 나눌 수 있는 수들이 있다.
A의 최대공약수의 약수들이다. 만약 gcd는 B를 나눌 수 있지만 약수들은 나눌 수 없다면
기존 로직이 틀린 것이다.
하지만 gcd로 나눌 수 있는 수들은 당연히 gcd의 약수로도 나눌 수 있다.
그리고 우리는 가장 큰 수를 찾아야 하므로 약수들은 검토할 필요가 없다.
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
