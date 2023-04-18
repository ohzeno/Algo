# https://school.programmers.co.kr/learn/courses/30/lessons/92342
"""
라이언: 전 우승자
어피치: 결승전 상대.
1. 어피치가 화살 n발을 다 쏜 후 라이언이 n발 쏜다.
2. 점수 계산
    1. 가장 작은 원 10점, 가장 바깥 원의 바깥은 0
    2. 만약 k(1~10)점을 어피치가 a발 맞히고 라이언이 b발 맞히면 더 많은 화살을
        k점에 맞힌 선수가 k점 가져감. 단, a = b이면 어피치가 k점 가져감. k점을
        여러 발 맞혀도 k점 보다 많은 점수 가져가지 않음. k점만 가져감.
        또, a = b = 0이면 둘 다 0점.
    3. 모든 과녁 점수에 대해 각 선수 최종 점수 계산.
3. 최종 점수가 더 높은 선수가 우승. 단, 점수가 같으면 어피치가 우승.
현재 라이언이 쏠 차례. 어피치를 가장 큰 점수 차이로 이기기 위해 n발을 어떻게 쏴야
하는지 구하려 한다.
화살 개수 n, 어피치가 맞힌 과녁 점수 개수를 10점부터 0점까지 순서대로 담은 info가 주어진다.
라이언이 맞춰야 하는 화살 수를 10점부터 0점까지 배열에 담아 return.
만약 라이언이 우승할 수 없는 경우, [-1]을 return.
라이언이 가장 큰 점수 차이로 우승할 방법이 여럿일 경우 가장 낮은 점수를 더 많이 맞힌 경우를 return
"""
def solution_dfs(n, info):
    cases = []
    max_p_dif = [0]
    a_point = [sum([i if info[-(i + 1)] else 0 for i in range(11)])]
    tmp = [0] * 11
    def dfs(cur, remain, point):
        nonlocal cases
        if not remain:
            dif = point - a_point[0]
            if dif and dif >= max_p_dif[0]:
                if dif > max_p_dif[0]:
                    cases = []
                    max_p_dif[0] = dif
                cases.append(tuple(reversed(tmp)))
            return
        for i in range(cur, 11):
            if remain > info[i]:
                for cnt in range(remain, info[i], -1):
                    tmp[i] = cnt
                    if info[i]:
                        a_point[0] -= 10 - i
                    dfs(i + 1, remain - cnt, point + (10 - i))
                    tmp[i] = 0
                    if info[i]:
                        a_point[0] += 10 - i
            else:
                for cnt in range(remain, -1, -1):
                    tmp[i] = cnt
                    dfs(i + 1, remain - cnt, point)
                    tmp[i] = 0
    dfs(0, n, 0)
    if not cases:
        return [-1]
    cases.sort(reverse=True)
    return list(reversed(cases[0]))

def solution2(n, info):
    def gen_cases(leng, tot):
        if leng == 1:
            return [[tot]]
        cases = []
        for i in range(tot + 1):
            cases += [[i] + case for case in gen_cases(leng - 1, tot - i)]
        return cases
    cases = gen_cases(11, n)
    def cal_diff(data):
        a, b = 0, 0
        for i in range(11):
            if data[i] > info[i]:
                a += (10 - i)
            elif info[i]:
                b += (10 - i)
        return a - b
    anss = []
    max_diff = 0
    for case in cases:
        tmp_dif = cal_diff(case)
        if tmp_dif > max_diff:
            max_diff = tmp_dif
            anss = [tuple(reversed(case))]
        elif max_diff and tmp_dif == max_diff:
            anss.append(tuple(reversed(case)))
    if not anss:
        return [-1]
    anss.sort(reverse=True)
    return list(reversed(anss[0]))

from itertools import product
def solution(n, info):
    def cal_diff(data):
        a, b = 0, 0
        for i in range(11):
            if data[i]:
                a += i
            elif info[i]:
                b += i
        return a - b
    info.reverse()  # 점수 낮은 쪽부터
    ans = [-1]
    max_dif = 0
    for win in product([1, 0], repeat=11):  # 점수는 승패만 알면 된다.
        tmp_dif = cal_diff(win)  # 이 승패에서의 점수차
        if tmp_dif > max_dif:  # 기존보다 점수차 크면
            """
            점수차가 같을 경우 가장 낮은 점수에 맞춘 화살 수가 큰 쪽을 선택해야 한다.
            이 순회는 가장 낮은 점수의 화살부터 체크하므로 
            점수차가 같은 경우는 확인할 필요 없다.
            """
            # 승패를 반영하는 최소 화살 수 배열
            tmp_ans = [info[i] + 1 if win[i] else 0 for i in range(11)]
            tmp_cnt = sum(tmp_ans)  # 최소 화살 수
            if tmp_cnt > n:  # 필요한 화살 수가 총 화살 수보다 많으면 제외
                continue
            max_dif = tmp_dif  # 최대 점수차 갱신
            ans = tmp_ans  # 최대 점수차 배열 갱신
            ans[0] += n - tmp_cnt  # 남은 화살은 가장 낮은 점수에 맞춘다.
    ans.reverse()  # 점수 높은 쪽부터
    return ans

inputdatas = [
    [5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
    [1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]],
    [10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]],
]

"""
2022 카카오 공채 기출. Lv.2. 현 시점 제출 5,195, 정답률 32%
제한사항에 정답 선택 조건이 더 나와있는데, 그걸 안읽어서 한 번 틀렸다.
이후 8, 15케이스를 틀렸는데 8케이스는 18과 함께 정렬문제인데, 나는 18은 통과했고
15는 질문 게시판에도 말이 없어서 원인을 찾지 못하는 중.

remain이 info[i]보다 작을 때, point가 a_point[0]보다 큰 경우만 순회를 돌게 해서 틀렸다.
n값이 작아서 dfs를 사용했는데 그냥 itertools로 모든 경우의 수 체크하는게 더 깔끔할 것 같다.

풀이를 2개 추가했다.
itertools 풀이도 꽤나 애먹었다. Lv.3과 Lv.4 사이의 느낌이다. 
모수가 작긴 하지만 정답률이 30%나 나온다니 고인물이 많긴 한가보다...
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
