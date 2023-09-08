# https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""
1~45
6개 번호 맞으면 1등
~2개 번호 맞으면 5등
lottos의 0은 지워진 번호.
가능한 최고 순위, 최저 순위를 구해서 리턴하라.
"""


def solution(lottos, win_nums):
    win_nums = set(win_nums)
    same = len(set(lottos) & win_nums)
    zeros = lottos.count(0)
    ans = [same + zeros, same]
    for i, case in enumerate(ans):
        ans[i] = 6 if case < 2 else 7 - case
    return ans


inputdatas = [
    [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]],
    [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]],
    [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]],
]

"""
현 시점 Lv.1. 완료한 사람 40,290명. 정답률 57%
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 기출.

쉬운 문제라는걸 눈치채기까지 몇 분 걸렸다.
베스트 풀이들을 보니 더 짧긴 한데 직관적이지 않고 가독성이 떨어졌다.
당첨 순위는 for문을 쓰는게 제일 직관적인 듯 하다.
"""

for t in inputdatas:
    print(solution(*t))
