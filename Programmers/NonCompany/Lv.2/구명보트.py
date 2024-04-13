# hhttps://school.programmers.co.kr/learn/courses/30/lessons/42885
"""
구명보트에 한 번에 최대 2명 탈 수 있고 무게 제한 있음.
구명보트를 최대한 적게 사용하여 모든 사람을 구출하려 함.
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 리턴하라.
제한사항
    무인도에 갇힌 사람은 1명 이상 50,000명 이하
    각 사람의 몸무게는 40kg 이상 240kg 이하
    무게 제한은 40kg 이상 240kg 이하
    무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없음.
"""


def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0
    while left <= right:
        # 가장 무거운 사람과 가장 가벼운 사람 조합 가능하면 같이 보냄
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1  # 같이 타든 안타든 무거운 사람은 타야함.
        cnt += 1
    return cnt


inputdatas = [
    {
        "data": [[70, 50, 80, 50], 100],
        "answer": 3,
    },
    {"data": [[70, 80, 50], 100], "answer": 3},
]

"""
구명보트. 탐욕법(Greedy)
Lv.2. 현 시점 완료한 사람 30,885명, 정답률 69%
무게 순 정렬 후, 가장 무거운 사람과 가장 가벼운 사람을 조합해보고,
제한을 넘지 않으면 보트에 태워보낸다.
    left += 1, right -= 1, cnt += 1
제한을 넘으면 무거운 사람만 따로 보낸다.
    right -= 1, cnt += 1
로직이 겹치므로 간략화하면 
    제한을 넘지 않으면 left += 1
    제한 여부와 무관하게 right -= 1, cnt += 1
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
