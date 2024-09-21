# https://school.programmers.co.kr/learn/courses/30/lessons/258712
"""
친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려 함

- 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음
    - 예를 들어 A가 B에게 선물을 5번 줬고,B가 A에게 선물을 3번 줬다면 다음 달엔 A가 B에게 선물을 하나 받음.
- 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음.
    - 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
    - 예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다.B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다. 만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 B가 A에게 선물을 하나 받음.
    - **만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않음.**

위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.

친구들의 이름을 담은 1차원 문자열 배열 friends, 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수로 주어짐. 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

### 제한사항
- 2 ≤ friends의 길이 = 친구 수 ≤ 50
    - friends의 원소는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열
    - 이름이 같은 친구는 없음.
- 1 ≤ gifts의 길이 ≤ 10,000
    - gifts의 원소는 "A B"형태의 문자열입니다. A는 선물을 준 친구의 이름을 B는 선물을 받은 친구의 이름을 의미하며 공백 하나로 구분됩니다.
    - A와 B는 friends의 원소이며 A와 B가 같은 이름인 경우는 존재하지 않음
"""


def solution(friends, gifts):
    n2i = {name: idx for idx, name in enumerate(friends)}
    len_f = len(friends)
    next_month = [0] * len_f
    # log[si][ri] = si가 ri에게 준 선물의 수
    log = [[0] * len_f for _ in range(len_f)]
    for gift in gifts:
        sn, rn = gift.split()
        log[n2i[sn]][n2i[rn]] += 1
    # 선물 지수. 준 선물 수 - 받은 선물 수
    # gi[si] = sum(log[si]) - sum(zip(*log)[si])
    gi = [sum(row) - sum(col) for row, col in zip(log, zip(*log))]
    for a in range(len_f):
        for b in range(a + 1, len_f):
            if log[a][b] > log[b][a]:  # a가 b에게 더 많이 줬다면
                next_month[a] += 1
            elif log[a][b] < log[b][a]:  # b가 a에게 더 많이 줬다면
                next_month[b] += 1
            # a, b끼리의 기록이 없거나(없으면 0이라 결국 같음) 같으면
            # 지수가 낮은 사람이 높은 사람에게 준다.
            elif gi[a] > gi[b]:
                next_month[a] += 1
            elif gi[a] < gi[b]:
                next_month[b] += 1
    return max(next_month)


inputdatas = [
    {
        "data": [["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]],
        "answer": 2,
    },
    {
        "data": [["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]],
        "answer": 4,
    },
    {
        "data": [["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]],
        "answer": 0,
    }
]

"""
2024 카카오 윈터 인턴십 기출.
Lv.1. 현 시점 완료한 사람 4242명, 정답률 23%
lv.4보다 정답률 10% 이상 낮은 lv.1이라니...
시험 당시에는 풀긴 했는데 코드가 50줄 이상이었다.

다른 사람 풀이에 간결한 것이 있어서 살펴봤는데,
로직은 나와 같고, 내가 give, receive 딕셔너리로 관리한 선물기록을 2차원 리스트로 관리했다.
하는 김에 나도 2차원 리스트로 간결화 하고 더 개선해봤다.
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
