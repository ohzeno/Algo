# https://school.programmers.co.kr/learn/courses/30/lessons/42897
"""
원형으로 배치.
각 집들을 털면 양쪽 집에 경보가 울림.
각 집에 있는 돈이 주어질 때, 훔칠 수 있는 돈의 최댓값을 return하라
3 <= len(money) <= 10^6
0 <= money[i] <= 1000
"""
def solution(money):
    l_money = len(money)
    dp = [0] * l_money
    # 첫번째 집을 털었을 때
    dp[0] = dp[1] = money[0]
    for i in range(2, l_money - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    max_money = dp[-2]
    # 첫번째 집을 털지 않았을 때
    dp = [0] * l_money
    dp[1] = money[1]
    for i in range(2, l_money):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    return max(max_money, dp[-1])

inputdatas = [
    [1, 2, 3, 1],
]

"""
동적계획법(Dynamic Programming)
Lv.4. 현 시점 완료한 사람 6,101명, 정답률 36%
스티커 모으기(2)랑 완전히 같은 로직의 문제라 5분도 안걸려서 풀었다.
"""

for t in inputdatas:
    print(solution(t))
