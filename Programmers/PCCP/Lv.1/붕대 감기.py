# https://school.programmers.co.kr/learn/courses/30/lessons/250137
"""
t초 동안 붕대 감으며 초당 x 체력 회복
t초 채우면 y만큼 추가 회복
공격당해서 기술 취소되거나 기술이 끝나면 붕대감기 시간 초기화.
모든 공격이 끝난 직후 남은 체력 리턴. 죽었으면 -1 리턴.

bandage: [시전 시간, 초당 회복량, 추가 회복량]
    1 ≤ 시전 시간 = t ≤ 50
    1 ≤ 초당 회복량 = x ≤ 100
    1 ≤ 추가 회복량 = y ≤ 100
1 ≤ health ≤ 1,000
1 ≤ len(attacks) ≤ 100
    attacks[i]: [공격 시간, 피해량]
    공격 시간을 기준으로 오름차순 정렬된 상태
    공격 시간은 모두 다름.
    1 ≤ 공격 시간 ≤ 1,000
    1 ≤ 피해량 ≤ 100
"""


def solution(bandage, max_hp, attacks):
    cast_t, heal_ps, addi_heal = bandage
    pre_t, hp = 0, max_hp
    for attack_t, damage in attacks:
        # 공격을 당하는 순간에는 체력을 회복할 수 없어 -1 해줘야한다.
        diff = max(attack_t - pre_t - 1, 0)
        gen_h, bonus_h = diff * heal_ps, diff // cast_t * addi_heal
        hp = min(hp + gen_h + bonus_h, max_hp) - damage
        pre_t = attack_t
        if hp <= 0:
            return -1
    return hp


inputdatas = [
    {
        "data": [[5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]],
        "answer": 5,
    },
    {
        "data": [[3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]],
        "answer": -1,
    },
    {
        "data": [[4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]],
        "answer": -1,
    },
    {
        "data": [[1, 1, 1], 5, [[1, 2], [3, 2]]],
        "answer": 3,
    },
]

"""
[PCCP 기출문제] 1번 / 붕대 감기
Lv.1. 현 시점 완료한 사람 5,132명, 정답률 33%
Lv.1주제에 Lv.4 카카오 기출보다 정답률이 낮은 이유는 함정 때문.
'공격을 당하는 순간에는 체력을 회복할 수 없습니다'가 함정이다.
1초에 첫 공격을 당하면 0초에서 1초 사이가 1초라도 hp gen이 이루어지지 않는다.
직관적이지 않은듯.
힐보다 공격을 먼저 판정한다고 적었다면 쉽게 풀릴 문제.
생각나는 대로 풀었는데 다른 짧은 풀이들이랑 로직이 별로 다르지 않다.
while, dict를 사용하는 긴 풀이들이 있던데, 왜 그리 어렵게 풀었는지 모르겠다.
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
