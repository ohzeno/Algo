# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        leng = len(prices)
        dp = [0] * leng
        for i in range(1, leng):
            dp[i] = max(dp[i-1] + prices[i] - prices[i-1], 0)  # 직접 살펴봐야 이해하기 쉬움.
        return max(dp)
        # min_price = prices[0]
        # max_profit = 0
        # for i in range(1, leng):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        # return max_profit

inputdatas = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Easy. dp로 먼저 접근했다. DP가 항상 어렵게 느껴졌고, 
시간을 엄청 많이 쓴건 아니지만 Easy임에도 약간 어렵게 느껴졌다.
아래 풀이처럼 최소구매가격, 최대수익을 갱신하는 방식으로 풀이하면 더 직관적이다.
min max 대신 if문을 사용하면 시간복잡도가 약간 줄어드는 것 같다.
"""