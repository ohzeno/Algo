# https://school.programmers.co.kr/learn/courses/30/lessons/258709
"""
A와 B가 n개의 주사위를 가지고 승부. 주사위의 6개 면에 각각 하나의 수가 쓰여 있으며, 각 면이 나올 확률은 동일. 각 주사위는 1 ~ n의 번호를 가지고 있으며, 주사위에 쓰인 수의 구성은 모두 다름.

A가 먼저 n/2개의 주사위를 가져가면 B가 남은 n/2개의 주사위를 가져감. 각각 가져간 주사위를 모두 굴린 뒤, 나온 수들을 합해 점수를 계산합니다. 점수가 더 큰 쪽이 승리하며, 점수가 같다면 무승부

A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가져가려 합니다.

n = 4인 예시
| 주사위 | 구성 |
| #1 | [1, 2, 3, 4, 5, 6] |
| #2 | [3, 3, 3, 3, 4, 4] |
| #3 | [1, 3, 3, 4, 4, 4] |
| #4 | [1, 1, 4, 4, 5, 5] |
- 예를 들어 A가 주사위 #1, #2를 가져간 뒤 6, 3을 굴리고, B가 주사위 #3, #4를 가져간 뒤 4, 1을 굴린다면 A의 승리. (6 + 3 > 4 + 1)

A가 가져가는 주사위 조합에 따라, 주사위를 굴린 1296가지 경우의 승패 결과를 세어보면
| A의 주사위 | 승 | 무 | 패 |
| --- | --- | --- | --- |
| #1, #2 | 596 | 196 | 504 |
| #1, #3 | 560 | 176 | 560 |
| #1, #4 | 616 | 184 | 496 |
| #2, #3 | 496 | 184 | 616 |
| #2, #4 | 560 | 176 | 560 |
| #3, #4 | 504 | 196 | 596 |

A가 승리할 확률이 가장 높아지기 위해선 주사위 #1, #4를 가져가야 함.

주사위에 쓰인 수의 구성을 담은 2차원 정수 배열 dice가 매개변수로 주어짐. 이때, 자신이 승리할 확률이 가장 높아지기 위해 A가 골라야 하는 주사위 번호를 **오름차순으로** 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성하라. 승리할 확률이 가장 높은 주사위 조합이 유일한 경우만 주어짐

### 제한사항
- 2 ≤ dice의 길이 = n ≤ 10
    - n은 2의 배수입니다.
    - dice[i]는 i+1번 주사위에 쓰인 6개의 수를 담고 있습니다.
    - dice[i]의 길이 = 6
    - 1 ≤ dice[i]의 원소 ≤ 100
"""
from itertools import combinations, accumulate


def get_score_d(dices):
    # sd[점수] = 경우의 수
    # 초기 경우의 수 카운팅을 위한 1. 순회 과정에서 0번째 인덱스는 0이 되니 괜찮음.
    sd = [1]
    for dice in dices:  # 각 주사위 순회
        l_dp = len(sd)
        # 주사위 최대값 추가한 점수까지 idx생성, 0으로 초기화
        new_sd = [0] * (l_dp + max(dice))
        for np in dice:  # 새 주사위 각 면에 대해
            for p in range(l_dp):  # 모든 기존 점수에 대해 더해짐.
                # 기존 케이스에서 점수만 더해졌지 경우의 수가 바뀐게 아니므로 sd[i] 그대로 더함.
                new_sd[p + np] += sd[p]
        sd = new_sd
    return sd


def solution(dice_list):
    n = len(dice_list)  # 주사위 개수
    max_p = -1  # 최대 승리 확률 초기화
    max_case = []
    # A가 고르는 모든 주사위 조합에 대해
    for idxs_A in combinations(range(n), n // 2):
        # n이 최대 10이라 for문 한번에 처리하지 않아도 됨. combi에 최대 5개 들어감.
        # A의 주사위 조합에 대한 점수 분포
        a_sd = get_score_d(dice_list[i] for i in idxs_A)
        # B의 주사위 조합에 대한 점수 분포
        b_sd = get_score_d(dice_list[i] for i in range(n) if i not in idxs_A)
        # B의 점수 분포 누적 배열 계산
        b_sd_acc = list(accumulate(b_sd))
        win_cnt = 0  # 현재 조합에서의 A의 승리 경우의 수
        l_b_acc = len(b_sd_acc)
        for p in range(1, len(a_sd)):
            # A의 주사위 합이 p인 경우의 수
            # B의 점수가 p 미만인 누적 경우의 수
            # 둘을 곱해서 더하면 A가 이기는 경우의 수
            win_cnt += b_sd_acc[min(p, l_b_acc) - 1] * a_sd[p]
        if win_cnt > max_p:  # 최대 승리 횟수, 주사위 조합 업데이트
            max_p = win_cnt
            max_case = idxs_A
    return [i + 1 for i in max_case]  # 주사위 번호 1부터 시작하도록 조정


inputdatas = [
    {
        "data": [
            [
                [1, 2, 3, 4, 5, 6],
                [3, 3, 3, 3, 4, 4],
                [1, 3, 3, 4, 4, 4],
                [1, 1, 4, 4, 5, 5],
            ]
        ],
        "answer": [1, 4],
    },
    {
        "data": [[[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]],
        "answer": [2],
    },
    {
        "data": [
            [
                [40, 41, 42, 43, 44, 45],
                [43, 43, 42, 42, 41, 41],
                [1, 1, 80, 80, 80, 80],
                [70, 70, 1, 1, 70, 70],
            ]
        ],
        "answer": [1, 3],
    },
]

"""
2024 KAKAO WINTER INTERNSHIP 기출. 
Lv.3. 현 시점 완료한 사람 770명, 정답률 18%
코테 당시 풀이는 지금 제출해보니 50점. 시간초과가 많았다. 
a가 고르는 모든 주사위 조합에 대해, product로 a와 b의 모든 경우의 수를 구해서
그걸 또 product로 매치시켜서 승패 횟수를 구했었다.
시간초과를 예상했었지만 더 좋은 방법을 생각하지 못했었다.

이번 풀이는 카카오 해설과 다른 사람의 풀이를 참고해서 작성해봤다.
a가 고르는 모든 주사위 조합을 구하는 것은 같다.
이후에 a와 b의 모든 경우의 수에 대해 경우의 수 카운팅을 진행해서 점수 분포 배열을 만든다.
여기까지는 시간복잡도가 비슷할 것이다.
이후 b의 점수 분포 배열을 누적합 배열로 만들고,
a의 각 점수 케이스에 대해 b가 a보다 낮은 점수인 경우의 수를 누적합 배열에서 가져온다.
그렇게 경우의 수를 곱해주면 a가 이기는 경우의 수이므로 이후 최대 승리 횟수를 업데이트 한다.

확률분포 카운팅과 누적합을 이용해, 이전에는 직접 매칭하며 승패를 구하던 부분을 최적화한 것이다.
확률분포 만드는 부분이 어려워서, 코테 상황에 작성할 수 있을지는 모르겠다.
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
