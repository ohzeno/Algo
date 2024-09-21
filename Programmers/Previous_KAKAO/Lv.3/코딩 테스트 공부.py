# https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""
알고력, 코딩력은 0 이상의 정수
알고력 1/ 시간 1
코딩력 1/ 시간 1
현재 풀 수 있는 문제를 풀어 알고력/코딩력 높임. 각 문제마다 상승량 고정
같은 문제 여러 번 풀 수 있음.

모든 문제들을 풀 수 있는 능력 얻는 최단시간?

0 <= alp(알고력), cop(코딩력) <= 150
1 <= len(problems) <= 100
problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태.
alp_req는 문제를 푸는데 필요한 알고력.
    0 ≤ alp_req ≤ 150
cop_req: 문제를 푸는데 필요한 코딩력.
    0 ≤ cop_req ≤ 150
alp_rwd: 문제를 풀었을 때 증가하는 알고력.
    0 ≤ alp_rwd ≤ 30
cop_rwd: 문제를 풀었을 때 증가하는 코딩력.
    0 ≤ cop_rwd ≤ 30
cost는 문제를 푸는데 드는 시간.
    1 ≤ cost ≤ 100

정확성 테스트 케이스 제한사항
    0 ≤ alp,cop ≤ 20
    1 ≤ problems의 길이 ≤ 6
        0 ≤ alp_req,cop_req ≤ 20
        0 ≤ alp_rwd,cop_rwd ≤ 5
        1 ≤ cost ≤ 10
"""
def solution(alp, cop, problems):
    max_alp = max_cop = 0
    for problem in problems:  # 문제들 중 가장 높은 알고력, 코딩력을 구함.
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    if max_alp <= alp and max_cop <= cop:  # 이미 모든 문제를 풀 수 있음.
        return 0
    # dp[i][j]: 알고력 i, 코딩력 j 달성까지 걸리는 최소 시간.
    dp = [[float('inf')] * (max_cop+1) for _ in range(max_alp+1)]
    # max_cop가 항상 cop보다 크다면 dp배열 크기를 줄이고 0,0에서 시작하겠지만
    # 조건상 cop가 더 클 수도 있다.
    # alp, cop중 한 쪽이 이미 최대치를 넘었을 경우 dp배열 범위를 넘어가므로
    # min으로 초기값을 조정함. 결과 왜곡은 걱정할 필요 없다.
    # 이렇게 되면 어차피 마지막 idx만 순회하기 때문.
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp[alp][cop] = 0
    for c_al in range(alp, max_alp+1):
        for c_cp in range(cop, max_cop+1):
            c_time = dp[c_al][c_cp]
            if c_al < max_alp:  # 범위 벗어나지 않으면 알고력 1 훈련
                dp[c_al+1][c_cp] = min(dp[c_al+1][c_cp], c_time + 1)
            if c_cp < max_cop:  # 범위 벗어나지 않으면 코딩력 1 훈련
                dp[c_al][c_cp+1] = min(dp[c_al][c_cp+1], c_time + 1)
            for al_rq, cp_rq, al_rw, cp_rw, cost in problems:
                # 풀 수 있는 문제면
                if c_al >= al_rq and c_cp >= cp_rq:
                    # 풀고 난 후 알고력, 코딩력에서의 누적 시간 갱신
                    n_al = min(c_al + al_rw, max_alp)
                    n_cp = min(c_cp + cp_rw, max_cop)
                    dp[n_al][n_cp] = min(dp[n_al][n_cp], c_time + cost)
    return dp[max_alp][max_cop]  # 목표값 달성시 누적 시간 반환



inputdatas = [
    [[10, 10, [[10,15,2,1,2],[20,20,3,3,4]]], 15],
    [[0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]], 13]
]

"""
2022 KAKAO TECH INTERNSHIP 기출. 
Lv.3. 현 시점 완료한 사람 2,168명, 정답률 22%
플래 달성하고도 dp는 항상 어렵다. 이게 Lv.3...?
카카오 해설을 보고 풀었다.
다익스트라로 푸는 방법이 있다는데 잘 상상이 안된다.
"""

for data, ans in inputdatas:
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
