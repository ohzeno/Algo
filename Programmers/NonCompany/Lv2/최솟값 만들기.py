# https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""
길이가 같은 배열 둘에서 각각 한 개의 숫자를 뽑아 두 수를 곱한다.
그 수를 누적해나가는 행위를 배열에 남은 숫자가 없을 때까지 반복.
이 때, 최종 결과의 최소치를 리턴하라.
배열 A, B의 크기 : 1,000 이하의 자연수
배열 A, B의 원소의 크기 : 1,000 이하의 자연수
"""

def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))


inputdatas = [
    {"data": [[1, 4, 2], [5, 4, 4]], "answer": 29},
    {"data": [[1, 2], [3, 4]], "answer": 10},
]

"""
연습문제
Lv.2. 현 시점 완료한 사람 36,298명, 정답률 78%
옛날에 자주 풀었던 문제고, 서로 다른 방향으로 정렬하면 된다.
직관적으로는 이해되긴 하는데, 수학적 증명은 한번도 본 적 없고, 하지도 못했다.
두 조합을 비교하는 지역 최적화는 쉬운데 전체 최적화를 증명하려면 어떻게 해야할지 모르겠다.
푼 사람 중 이걸 증명하고 푼 사람이 존재하긴 할까?
오히려 수학적 감각이 좀 떨어지는 사람이 증명을 생각 안해서 더 쉽게 푸는 류의 문제다.

잠시 찾아보니 재배열 부등식이라고 수학경시대회에 나오는 문제인데,
증명이랍시고 나오는 것이 그리디 알고리즘이다. 임의의 두 항을 교환했을 때 전체 합이 더 커지므로
저게 최소라는 것을 증명이라고 주장하는데, 그건 두 항끼리 교환을 했으니 당연한 것이다.
지역 최적화만 고려하고 그걸 증명이라고 하니 어이가 없다.
예를 들면, 12, 21를 11, 22로 바꾸면 커진다는 것이다.
위는 두 항끼리만 교체한 것이므로 11 23 32가 13 22 31보다 작은지의 증명이 안된다.
방금 예시는 3개의 항이 재배열되어 두 항끼리의 비교만으로 증명할 수 없기 때문이다.
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
