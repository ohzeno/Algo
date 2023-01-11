# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product
def solution(users, emoticons):
    """
    1. 플러스 가입자 최대한 늘릴 것
    2. 이모티콘 판매액 최대한 늘리는 것.
    1번이 우선. n명 사용자에게 이모티콘 m개 할인판매
    이모티콘마다 할인율 다를 수 있고 10 % 단위로 10~40% 중 하나.
    각 사용자는 자신 기준에 따라 일정 비율 이상 할인하는 이모티콘 모두 구매.
    그 비용이 일정 가격 이상이면 구매 취소하고 플러스 가입.
    users 길이: 1~100
        [비율, 가격] 비율 이상 할인하는 이모티콘 구매, 가격 이상이면 플러스 가입
        users[i]: i+1번 고객 구매기준
        가격: 100~100만. 100의 배수.
    emoticons 길이: 1~7
        emoticons[i]: i+1번 이모티콘 정가
        emoticons 원소 100~100만. 100의 배수
    """
    sale_data = [10, 20, 30, 40]
    sale_cases = product(sale_data, repeat=len(emoticons))  # 세일 경우의 수
    answer = [0, 0]
    for case in sale_cases:  # 경우의 수 순회
        plus, tot = 0, 0  # 해당 케이스 플러스 가입자, 이모티콘 매출
        for user_sale, user_limit in users:  # 유저 순회
            acc = 0  # 유저가 구매한 이모티콘 누적 가격
            for emo_idx, emo_sale in enumerate(case):  # 이모티콘 번호, 할인율
                if emo_sale >= user_sale:  # 유저 구매기준보다 할인율 높으면
                    acc += emoticons[emo_idx] * (1 - emo_sale/100)  # 구매
            if acc >= user_limit:  # 누적 가격이 제한 넘으면 플러스로
                plus += 1
            else:  # 제한 넘지 않으면 케이스 총 가격에 더해준다.
                tot += acc
        answer = max(answer, [plus, int(tot)])  # 기존 기록과 현 케이스 중 플러스, 매출이 큰 쪽을 기록.
    return answer

inputdatas = [
    [[
        [40, 10000], [25, 10000]
    ], [7000, 9000]],
    [[
        [40, 2900], [23, 10000], [11, 5200],
        [5, 5900], [40, 3100], [27, 9200], [32, 6900]
    ], [1300, 1500, 1600, 4900]]
]

"""
2023 카카오 공채 기출. Lv.2 현 시점 제출 77명 정답률 16%.
설계 완전히 잘못해서 1시간 날렸다. 
이모티콘별 할인율이 고정이어야 하는데 유저별로 할인율 따라 dfs돌아서 결과가 다르게 됐다.
코테 당시 itertools 사용해서 풀었었는데 시간 효율성 챙기겠다고 딕셔너리 쓰다가 이렇게 됐다.
알고보니 코테 당시 풀이에 시간초과가 없었다...그냥 itertools 사용했으면 금방 풀었을듯...

itertools를 사용해 새로 풀어보니 10분 걸렸다.
당시 풀이, 현재 풀이가 거의 똑같은 진행과정이다.
베스트 풀이(현재 좋아요 1)가 내 풀이와 로직이 완벽히 일치해서 놀랐다. 
zip, enumerate가 대응되는 점, 나는 int로 소수점 처리를 해준 점을 제외하면 로직이 완전히 같다.
for, if 위치도 같고 for에서 언패킹 하는 점도 같다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
