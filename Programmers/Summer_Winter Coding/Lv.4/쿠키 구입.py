# https://school.programmers.co.kr/learn/courses/30/lessons/49995
"""
첫째 아들에게는 i번 ~ m번 바구니
둘째 아들에게 m+1번 ~ r번 바구니
두 아들이 받을 과자 수는 같아야 함.
(1 <= i <= m, m+1 <= r <= n)
조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 리턴하라.
조건에 맞게 구매할 수 없으면 0을 리턴
"""
from itertools import accumulate


def solution(cookie):
    # max_cookies = 0
    # len_cookies = len(cookie)
    # for ll in range(len_cookies-1):
    #     rr = ll + 1
    #     son1, son2 = cookie[ll], cookie[rr]
    #     while True:
    #         if son1 == son2:
    #             max_cookies = max(max_cookies, son1)
    #         if son1 > son2 and rr + 1 < len_cookies:
    #             rr += 1
    #             son2 += cookie[rr]
    #         elif son1 <= son2 and ll - 1 >= 0:
    #             ll -= 1
    #             son1 += cookie[ll]
    #         else:
    #             break
    # return max_cookies
    max_cookies = 0
    for mid in range(len(cookie) - 1):
        # accumulate는 순회돌면서 누적합을 모아서 iterator로 반환해준다.
        son1 = set(accumulate(reversed(cookie[: mid + 1])))
        son2 = set(accumulate(cookie[mid + 1 :]))
        match = son1 & son2  # 동등하게 나눠진 케이스들
        if match:  # 동등하게 나눠진 케이스가 있으면
            max_cookies = max(max_cookies, *match)  # 최대값 갱신
    return max_cookies


inputdatas = [
    [1, 1, 2, 3],
    [1, 2, 4, 5],
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.4. 현 시점 완료한 사람 1,522명, 정답률 29%
나는 투포인터를 이용했는데 베스트 풀이를 보니 accumulate라는 함수를 썼다.
사용해보니 상당히 편리하다. 
거기다, for문은 조건에 따라서 포인터를 움직이고 가지치기가 되었고
포인터 개념으로는 accumulate는 가지치기가 없음에도 불구하고
accumulate를 사용한 풀이가 훨씬 빠르다.
아마 c로 구현되어 있어서 그런듯.
"""

for t in inputdatas:
    print(solution(t))
