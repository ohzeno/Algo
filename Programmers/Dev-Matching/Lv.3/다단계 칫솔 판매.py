# https://school.programmers.co.kr/learn/courses/30/lessons/77486
"""
판매원은 모든 수익에 대해 추천인에게 10%를 배분한다.
단, 10% 금액은 원 단위로 절사한다.
원 단위로 절사한다는 뜻은 내림이라는 뜻. 1.5원이면 1원.
10%가 0.9원이면 0원
레퍼럴로 받은 수익도 추천인(레퍼럴)에게 10%를 배분한다.
enroll: 판매원 이름들
referral: 판매원들의 추천인 이름들
seller: 물건 판 판매원들
amount: 판 물건 양 (개당 100원)
각 판매원 수익을 정수형으로 enroll 순서대로 배열에 담아 리턴하라.
"""


def solution(enroll, referral, sellers, amounts):
    accounts = {person: 0 for person in enroll}
    parents = dict(zip(enroll, referral))
    for seller, amount in zip(sellers, amounts):
        total = amount * 100
        while not (total == 0 or seller == '-'):  # 센터는 집계 안함
            accounts[seller] += total
            total //= 10  # 10% 절사
            accounts[seller] -= total  # 추천인에게 줄 10%를 뺌
            seller = parents[seller]  # 추천인으로 올라감
    return list(accounts.values())


inputdatas = [
    [
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
    ],
    [
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["sam", "emily", "jaimie", "edward"],
        [2, 3, 5, 4],
    ],
]

"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 기출. 
Lv.2. 현 시점 완료한 사람 5,522명, 정답률 39%
평범한 구현 문제.
인자들 이름이 좀 이상하다. 
sellers, amounts는 처음에 단수로 들어와서 내가 바꿨다.
"""

for t in inputdatas:
    print(solution(*t))
