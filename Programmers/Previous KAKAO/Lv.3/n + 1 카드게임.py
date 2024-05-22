# https://school.programmers.co.kr/learn/courses/30/lessons/258707
"""
당신은 1~n 사이의 수가 적힌 카드가 하나씩 있는 카드 뭉치와
동전 coin개를 이용한 게임을 하려고 합니다.
카드 뭉치에서 카드를 뽑는 순서가 정해져 있으며, 게임은 다음과 같이 진행합니다.

1. 카드 뭉치에서 카드 n/3장을 뽑아 가짐. (n은 6의 배수입니다.) 당신은 카드와 교환 가능한 동전 coin개를 가지고 있습니다.
2. 게임은 1라운드부터 시작되며, 각 라운드가 시작할 때 카드를 두 장 뽑음. 카드 뭉치에 남은 카드가 없다면 게임을 종료. 뽑은 카드는 장당 동전 하나를 소모해 가지거나, 동전을 소모하지 않고 버릴 수 있음.
3. 카드에 적힌 수의 합이 n+1이 되도록 카드 두 장을 내고 다음 라운드로 진행할 수 있음. 만약 카드 두 장을 낼 수 없다면 게임을 종료.

ex) n = 12, coin = 4이고 [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]가 카드 순서일 때
처음에 3, 6, 7, 2 카드 4장(= n/3)과 동전 4개(= coin)를 가지고 시작합니다. 다음 라운드로 진행하기 위해 내야 할 카드 두 장에 적힌 수의 합은 13(= n+1)입니다. 다음과 같은 방법으로 최대 5라운드까지 도달할 수 있습니다.

1. 1라운드에서 뽑은 카드 1, 10을 동전 두 개를 소모해서 모두 가짐. 카드 3, 10을 내고 다음 라운드로 진행. 손에 남은 카드는 1, 2, 6, 7이고 동전이 2개 남음.
2. 2라운드에서 뽑은 카드 5, 9를 동전을 소모하지 않고 모두 버립니다. 카드 6, 7을 내고 다음 라운드로 진행. 손에 남은 카드는 1, 2고 동전이 2개 남음.
3. 3라운드에서 뽑은 카드 8, 12 중 동전 한 개를 소모해서 카드 12를 가짐. 카드 1, 12을 내고 다음 라운드로 진행. 손에 남은 카드는 2이고 동전이 1개 남음.
4. 4라운드에서 뽑은 카드 11, 4 중 동전 한 개를 소모해서 카드 11을 가짐. 카드 2, 11을 내고 다음 라운드로 진행. 손에 남은 카드와 동전은 없음.
5. 5라운드에서 카드 뭉치에 남은 카드가 없으므로 게임을 종료.

처음에 가진 동전수 coin과 뽑을 카드를 순서대로 담은 1차원 정수 배열 cards가 매개변수로 주어질 때, 게임에서 도달 가능한 최대 라운드의 수를 return 하도록 solution 함수를 완성하라.

### 제한사항
- 0 ≤ coin ≤ n
- 6 ≤ cards의 길이 = n < 1,000
    - cards[i]는 i+1번째로 뽑는 카드에 적힌 수를 나타냅니다.
    - 1 ≤ cards[i] ≤ n
    - cards의 원소는 중복되지 않습니다.
- n은 6의 배수입니다.
"""


def solution(coin, cards):
    def remove_pair_if_exists(deck1, deck2):
        for c1 in deck1:
            if target - c1 in deck2:
                deck1.remove(c1)
                deck2.remove(target - c1)
                return True
        return False
    n = len(cards)
    target = n + 1
    st = n // 3
    hands = set(cards[:st])  # 처음에 손에 든 카드
    not_selected = set()  # 뽑았지만 아직 코인으로 가져오지 않은 카드
    round = 0
    for i in range(st, n, 2):
        round += 1
        not_selected.update(cards[i:i+2])
        if remove_pair_if_exists(hands, hands):  # 손에 있는 카드로 뽑은 카드를 내는 경우
            continue
        elif coin >= 1 and remove_pair_if_exists(hands, not_selected):
            # 코인 1개로 카드 가져오는 경우
            coin -= 1
        elif coin >= 2 and remove_pair_if_exists(not_selected, not_selected):
            # 코인 2개로 카드 가져오는 경우
            coin -= 2
        else:  # 더 이상 진행할 수 없는 경우
            return round
    return round + 1  # 마지막 라운드까지 진행한 경우


inputdatas = [
    {"data": [4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]], "answer": 5},
    {"data": [3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]], "answer": 2},
    {"data": [2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]], "answer": 4},
    {
        "data": [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]],
        "answer": 1,
    },
]

"""
2024(실제 시험은 2023) 카카오 겨울 인텁십 기출. 
Lv.3. 현 시점 완료한 사람 787명, 정답률 17%
시간초과를 해결하지 못해서 해설을 봤다.
시간초과가 발생한 이유는, 매 라운드에서 카드 선택 가능성 조합을 모두 검토했기 때문이다.

1라운드에 코인을 0~2개 소모할 수 있을 때, 어느 것이 최종적으로 최적해인지 모른다.
1라운드에 0개 소모하면 카드조합이 망가져 3라운드까지밖에 못갈 수도 있고,
1라운드에 2개 소모했지만 5라운드까지 갈 수도 있다.
그래서 모든 가능성을 검토한 것인데,
해설을 보니 매 라운드 코인 소모를 가장 적게 선택한다. 이게 가능한 이유가
카드를 매 라운드에서 바로 버리거나 선택하지 않고 진행한 후에 
과거의 카드 조합을 보면서 선택할 수 있기 때문이다.
그러면 해당 라운드까지의 최적 경로가 자동으로 선택된다.
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
