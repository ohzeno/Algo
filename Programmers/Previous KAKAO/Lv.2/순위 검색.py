# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from bisect import bisect_left
def solution(info, query):
    """
    코테 참여 개발언어: cpp, java, python
    직군: backend, frontend
    경력구분: junior, senior
    소울푸드: chicken, pizza
    조건을 만족하는 사람 중 코테 x점 이상 몇 명? 이라는 형태의 문의.
    info: 지원자 정보,    query: 쿼리
    각 문의조건에 해당하는 사람들의 수를 순서대로 배열에 담아 리턴.
    info 크기 1~5만. 점수는 1~10만
    query 크기 1~10만
    -는 고려x,
    """
    user_info = {}
    answer = []
    for idx, data in enumerate(info):
        langs, fbs, levs, foods, scores = data.split()
        scores = int(scores)
        # 모든 쿼리 경우의 수를 키값으로 점수를 넣어준다.
        for lang in [langs, '-']:
            for fb in [fbs, '-']:
                for lev in [levs, '-']:
                    for food in [foods, '-']:
                        key = (lang, fb, lev, food)
                        user_info.setdefault(key, []).append(scores)
    for user in user_info:  # 이분 탐색을 위해 정렬
        user_info[user].sort()
    for q in query:
        q_lang, q_fb, q_lev, q_food = q.split(' and ')
        q_food, q_score = q_food.split()
        q_score = int(q_score)
        # 키값이 없는 경우도 있기에 get으로 접근
        datas = user_info.get((q_lang, q_fb, q_lev, q_food), [])
        tot = len(datas)
        # 오름차순에서 왼쪽부터 탐색. q_score 이상인 값의 인덱스 반환. 없으면 0
        ll = bisect_left(datas, q_score)
        # 이분탐색
        # ll, rr = 0, tot-1
        # while ll <= rr:
        #     mid = (ll + rr) // 2
        #     if datas[mid] >= q_score:
        #         rr = mid - 1
        #     else:
        #         ll = mid + 1
        answer.append(tot - ll)  # tot가 2고 ll이 1이면 datas[1]만 조건을 만족.
    return answer

inputdatas = [
    [
        ["java backend junior pizza 150",
         "python frontend senior chicken 210",
         "python frontend senior chicken 150",
         "cpp backend senior pizza 260",
         "java backend junior chicken 80",
         "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
     ]
]

"""
2021 카카오 공채 기출. Lv.2. 현 시점 완료 6,883명, 정답률 33%
30분 초안 제출, 효율성 0점.
39분 2안 제출, 효율성 0점.
1시간 9분 3안 제출. 통과.
쿼리 경우의 수를 전부 key로 넣어주면 시간이 소모될거라 생각했는데, 그게 정답이었다.
key값에 점수 목록을 넣어놓고 정렬한다. 정렬과정에서 시간이 소요되는데
이후 쿼리에 대해 바로 점수 목록을 가져오고, 이분탐색으로 위치를 찾아 갯수를 계산하면 효율성을 통과한다.
이분탐색을 직접 구현했었는데, 몇 번 봤던 bisect_left를 사용해봤는데 상당히 편리했다.
구현 과정에서 while문을 빠져나오는 경우의 수를 생각하지 않아도 되고, 
조건문의 =여부도 생각하지 않아도 된다.
Lv.2 치고는 상당히 어려웠던 문제. 실제 코테에서 처음 만났으면 Lv.3보다 어렵게 느껴졌을 듯.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
