# https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""
constraints:
  • clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
  • 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
  • 같은 이름을 가진 의상은 존재하지 않습니다.
  • clothes의 모든 원소는 문자열로 이루어져 있습니다.
  • 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
"""

def solution(clothes):
    categories = {}
    for cloth, category in clothes:
        # 선택하지 않는 경우의 수 1
        categories[category] = categories.get(category, 1) + 1
    tot = 1
    for v in categories.values():
        tot *= v
    # - 모두 선택하지 않는 경우의 수
    return tot - 1


inputdatas = [
    {"data": [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]], "answer": 5},
    {"data": [[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]], "answer": 3}
]


"""
해시
Lv.2. 현 시점 완료한 사람 67,245명, 정답률 67%
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
