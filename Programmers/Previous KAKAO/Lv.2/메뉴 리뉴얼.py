# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
def solution(orders, course):
    # orders: 각 손님들이 주문한 단품메뉴
    # course: 추가하고 싶은 코스요리 구성 단품메뉴 갯수
    # 함께 주문한 경우가 많은 순으로 배열에 넣어 리턴
    menus = []
    for i in course:  # 세트 구성 메뉴 갯수 순회
        set_dic = {}  # 카운팅을 위한 딕셔너리
        for order in orders:  # 개인 주문 순회
            datas = list(combinations(list(order), i))  # i개로 구성된 조합 리스트
            for data in datas:  # 각 조합 순회
                data = ''.join(sorted(data))  # 정렬해서 스트링으로
                if data not in set_dic:  # 딕셔너리 카운팅
                    set_dic[data] = 1
                else:
                    set_dic[data] += 1
        if set_dic:  # 조합이 존재한다면
            max_count = max(list(set_dic.values()))  # 최빈값
            if max_count > 1:  # 최빈값 2 이상만 취급함.
                for menu, count in set_dic.items():  # 조합 순회돌며
                    if count == max_count:  # 최빈값 메뉴만 추가
                        menus.append(menu)
    menus.sort()  # 정렬하고 리턴
    return menus

inputdatas = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]],
    [["XYZ", "XWY", "WXA"], [2, 3, 4]],
]

"""
2021 카카오 공채 기출. Lv.2. 옮겨적고 문제 읽고 이해하기까지 7분 좀 덜 사용했다고 생각했다.
구현 후 결과가 이상했다. 알고보니 문제를 잘못 이해한 상태였다. 
course의 각 원소는 구성하고픈 세트메뉴의 단품 갯수이며
해당 갯수 별로 가장 많은 횟수의 주문이 들어온 구성만 채택한다.
처음에는 갯수에 상관없이 주문이 2회 이상 들어온 메뉴를 다 리턴했더니 갯수가 엄청나게 많았다...
그리고 combinations로 나온 경우의 수 각각이 정렬이 안된 상태여서 원하는 출력이 나오지 않았다.
datas의 원소들 각각을 정렬하도록 map을 사용해볼까 1분 미만 고민하다가
key를 만들 때는 data를 스트링으로 만드니 그 때 정렬해서 하도록 바꿨다.
최종 제출까지 대략 35분쯤 걸린 듯 한데 타이머를 잘못 건드려서 정확한 시간은 아니다.
베스트 풀이를 보니 collections.Counter().most_common()을 사용해서 굉장히 짧게 작성했다.
most_common은 커녕 Counter도 배우지 않은 상태라 다음을 기약했다.
combinations를 이미 사용한 상태에서 말하긴 뭣하지만 
패키지를 너무 사용하면 패키지 없이 푸는 방법을 잊어 
파이썬 지원 안되는 곳에서 JS로 코테칠 때 힘들거라 생각한다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
