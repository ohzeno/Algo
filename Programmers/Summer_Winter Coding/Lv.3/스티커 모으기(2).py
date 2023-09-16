# https://school.programmers.co.kr/learn/courses/30/lessons/12971
"""
N개 스티커가 원형으로 연결되어 있음.
몇 장의 스티커를 뜯어내어,
뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하려고 함.
단, 뜯어낸 스티커 양쪽 스티커는 찢어져서 사용할 수 없음.
최대값 리턴.
1 <= len(sticker) <= 100,000
1 <= sticker[i] <= 100
"""


def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp = [0] * n
    # 첫 스티커 뜯는 경우
    dp[0] = sticker[0]
    dp[1] = sticker[0]  # 두 번째는 찢어졌으니
    for i in range(2, n - 1):  # 마지막 스티커는 찢어졌으니 제외
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    max_sum = dp[-2]
    dp = [0] * n
    # 첫 스티커 뜯지 않는 경우
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    return max(max_sum, dp[-1])


inputdatas = [[14, 6, 5, 11, 3, 9, 2, 10], [1, 3, 2, 5, 4]]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.3. 현 시점 완료한 사람 3,219명, 정답률 49%

dfs로 어떻게 해보려다가 포기했다.
dp로도 풀어보려 했지만 주변 스티커가 찢어진다는 제약때문에
어떻게 해야할지 감이 안 잡혔었다.

결국 힌트를 보고 풀었다.
원형이라는 특수성은 첫 스티커를 뜯는 경우, 아닌 경우를 나눠서 생각하면 된다.
스티커를 건들지 않는 경우 dp[i - 1]
스티커를 찢는 경우 dp[i - 2] + sticker[i]
이렇게 누적해가면 각 스티커의 상태에 대해 기억할 필요가 없다.

dp는 항상 어려운듯.
"""

for t in inputdatas:
    print(solution(t))
