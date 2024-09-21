# https://school.programmers.co.kr/learn/courses/30/lessons/258705
"""

"""


def solution(n, tops):
    """
    i번째 아래 방향 삼각형을 모두 덮은 후, 빈 곳을 정삼각형으로 채운다.
    i번째 아래 방향 삼각형을 덮는 방법의 수를 구할 때, 다음과 같은 4가지 방법이 있다.
    1. 위쪽 삼각형과 함께 마름모 타일로 덮는다.
    2. 왼쪽 삼각형과 함께 마름모 타일로 덮는다.
    3. 오른쪽 삼각형과 함께 마름모 타일로 덮는다.
    4. 정삼각형 타일로 덮는다.

    right[i]: i번째 아래 방향 삼각형을 3번 방법으로 덮는 경우의 수
    not_right[i]: i번째 아래 방향 삼각형을 1, 2, 4번 방법으로 덮는 경우의 수

    case1. i번째 아래 방향 위에 삼각형이 있는 경우(tops[i] == 1)
        right의 경우 무조건 3번을 쓸 수 있다. 즉
        right[i] = right[i-1] + not_right[i-1]

        not_right의 경우
            right[i-1]에서 3번을 썼으므로 i번 블럭 왼쪽은 막혀있어 1, 4번만 쓸 수 있다.
            not_right[i-1]는 오른쪽에 영향이 없으므로 1, 2, 4 모두 가능하다.
        not_right[i] = 2*right[i-1] + 3*not_right[i-1]

    case2. i번째 아래 방향 위에 삼각형이 없는 경우(tops[i] == 0)
        right의 경우 무조건 3번을 쓸 수 있다. 즉
        right[i] = right[i-1] + not_right[i-1]

        not_right의 경우
            right[i-1]에서 3번을 썼으므로 i번 블럭 왼쪽은 막혀있어 1, 4번만 쓸 수 있다.
            하지만 위가 없으므로 1번도 쓸 수 없다. 4번만 남는다.
            not_right[i-1]는 오른쪽에 영향이 없으므로 1, 2, 4 모두 가능하다.
            하지만 위가 없으므로 1번은 쓸 수 없다. 2, 4번만 남는다.
        not_right[i] = 1*right[i-1] + 2*not_right[i-1]
    """
    MOD = 10007
    right = [0] * n
    not_right = [0] * n
    right[0] = 1
    not_right[0] = 3 if tops[0] else 2
    for i in range(1, n):
        right[i] = (right[i-1] + not_right[i-1]) % MOD
        a, b = (2, 3) if tops[i] else (1, 2)
        not_right[i] = (a*right[i-1] + b*not_right[i-1]) % MOD
    return (right[-1] + not_right[-1]) % MOD


inputdatas = [
    {"data": [4, [1, 1, 0, 1]], "answer": 149},
    {"data": [2, [0, 1]], "answer": 11},
    {"data": [10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "answer": 7704},
]

"""
2024 KAKAO WINTER INTERNSHIP 기출.
Lv.3. 현 시점 완료한 사람 884명, 정답률 23%
dp를 써야한다는 건 알았는데, 점화식을 만들지 못했다.
카카오 해설을 본 후에 풀었다.
시험 당시에는 시간이 더 있어도 못풀었을 것 같다. 이게 Lv.3이 맞나...?
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
