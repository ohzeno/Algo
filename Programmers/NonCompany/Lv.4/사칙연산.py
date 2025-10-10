# https://school.programmers.co.kr/learn/courses/30/lessons/1843
"""
constraints:

"""


def solution(arr):
    numbers = []
    operators = []
    for i in range(len(arr)):
        if i % 2 == 0:
            numbers.append(int(arr[i]))
        else:
            operators.append(arr[i])
    n = len(numbers)
    # dp_max[i][j]: i부터 j까지의 연산결과 최댓값
    # dp_min[i][j]: i부터 j까지의 연산결과 최솟값
    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]
    for length in range(2, n + 1):  # 구간 길이
        for ll in range(n - length + 1):
            rr = ll + length - 1
            # 구간을 두 파트로 분할
            for mid in range(ll, rr):
                if operators[mid] == '+':
                    # 덧셈은 최댓값끼리, 최솟값끼리
                    dp_max[ll][rr] = max(
                        dp_max[ll][mid] + dp_max[mid + 1][rr],
                        dp_max[ll][rr]
                    )
                    dp_min[ll][rr] = min(
                        dp_min[ll][mid] + dp_min[mid + 1][rr],
                        dp_min[ll][rr]
                    )
                else:  # 마이너스
                    dp_max[ll][rr] = max(
                        dp_max[ll][mid] - dp_min[mid + 1][rr],
                        dp_max[ll][rr],
                    )
                    dp_min[ll][rr] = min(
                        dp_min[ll][mid] - dp_max[mid + 1][rr],
                        dp_min[ll][rr],
                    )
    return dp_max[0][n - 1]


inputdatas = [
    {"data": [["1", "-", "3", "+", "5", "-", "8"]], "answer": 1},
    {"data": [["5", "-", "3", "+", "1", "+", "2", "-", "4"]], "answer": 3}
]


"""
동적계획법(Dynamic Programming)
Lv.4. 현 시점 완료한 사람 3,241명, 정답률 18%
비슷한 문제를 몇년 전에 풀어봤던 것 같은데 잘 기억 안난다.
3차원dp 혹은 2차원dp 둘로 해결했던 것 같다.
오랜만에 복잡한 dp라 구조 떠올리기가 까다로웠다.
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
