# https://school.programmers.co.kr/learn/courses/15008/lessons/121684
"""
여러 종목에 대해 각 반의 해당 종목 대표가 1명씩 나와 대결.
한 학생은 최대 한개의 종목 대표만 가능.
강 종목 대표의 해당 종목 능력치 합을 최대화하려고 함.
강 종목 대표의 능력치 합 최대치를 리턴하라.
"""
from itertools import permutations


def solution(ability):
    n, m = len(ability), len(ability[0])
    max_sum = 0
    # 학생 조합
    for case in permutations(range(n), m):
        local_sum = 0
        # 순차적으로 종목 배정
        for i, p in enumerate(case):
            local_sum += ability[p][i]
        max_sum = max(max_sum, local_sum)
    return max_sum



inputdatas = [
    [[[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]], 210],
    [[[20, 30], [30, 20], [20, 30]], 60],
]

"""
[PCCP 모의고사 #1] 2번 - 체육대회
dfs나 dp를 생각했다가, 사람을 고르는 경우의 수가 다르다는 것을 인지하고
조합을 사용하려다가 사람을 같은 조합으로 뽑아도 종목을 다르게 정해야 해서
결국 순열을 사용.
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
