# https://leetcode.com/problems/k-inverse-pairs-array/
import sys
from typing import Optional, List

"""
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 10^9 + 7.

constraints:
1 <= n <= 1000
0 <= k <= 1000
"""
from functools import cache
sys.setrecursionlimit(10**7)

class Solution:
    # def kInversePairs(self, n: int, k: int) -> int:
    #     dp = [[0] * (k + 1) for _ in range(n + 1)]
    #     MOD = 10**9 + 7
    #     dp[1][0] = 1
    #     for r in range(2, n + 1):
    #         dp[r][0] = 1
    #         max_k = r * (r - 1) // 2
    #         for c in range(1, min(max_k, k)+1):
    #             dp[r][c] = dp[r][c-1] + dp[r-1][c] - (dp[r-1][c-r] if c >= r else 0)
    #             dp[r][c] %= MOD
    #     return dp[n][k]
    # def kInversePairs(self, n: int, k: int) -> int:
    #     # 리스트 2개로 메모리 최적화
    #     MOD = 10**9 + 7
    #     prev = [0] * (k + 1)
    #     cur = [0] * (k + 1)
    #     prev[0] = cur[0] = 1
    #     for r in range(2, n + 1):
    #         max_k = r * (r - 1) // 2
    #         for c in range(1, min(max_k, k) + 1):
    #             cur[c] = cur[c - 1] + prev[c] - (prev[c - r] if c >= r else 0)
    #             cur[c] %= MOD
    #         prev = cur[:]
    #     return cur[k]
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        max_k = n * (n - 1) // 2
        if k > max_k:
            return 0
        if k == 0 or k == max_k:
            return 1
        return (
            self.kInversePairs(n, k - 1) +
            self.kInversePairs(n - 1, k) -
            (self.kInversePairs(n - 1, k - n) if k >= n else 0)
        ) % (10**9 + 7)



inputdatas = [
    {"data": [1, 0], "answer": 1},
    {"data": [3, 0], "answer": 1},
    {"data": [3, 1], "answer": 2},
    {"data": [2, 2], "answer": 0},
]

"""
LeetCode Hard.
제출 253.2K, 정답률 50.0%

이해하기 상당히 힘든 문제.
n이 증가했을 때, n-1 수열에서 어디에 n을 배치하느냐에 따라 역전쌍 수를 조절할 수 있다.
n이 4일 때, 1~3 순열에 4를 추가하는 경우를 생각해보자.
4 x x x는 3개의 역전쌍이 추가된다.
x 4 x x는 2개의 역전쌍이 추가된다.
x x 4 x는 1개의 역전쌍이 추가된다.
x x x 4는 0개의 역전쌍이 추가된다.
dp[n][k]는 n개의 수열에서 k개의 역전쌍을 가지는 경우의 수이므로
k개를 만들기 위해서는 dp[n-1][k-x]에 x개의 역전쌍을 추가해야한다.
dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... + dp[n-1][k-(n-1)]
두번째 인덱스가 음수가 되면 안되므로 k에서 빼는 수는 min(n, k+1)로 제한한다.
이렇게 하면 시간초과가 발생한다.

dp[n][k-1] = dp[n-1][k-1] + ... + dp[n-1][k-(n-1)] + dp[n-1][k-n]
dp[n][k]에서 이 식을 빼면
dp[n][k] - dp[n][k-1] = dp[n-1][k] - dp[n-1][k-n]
dp[n][k] = dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n] (k >= n)

k < n인 경우에는 (n > 1도 필요하다. n-1을 참조해야 하니.)
dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... + dp[n-1][0]
dp[n][k-1] = dp[n-1][k-1] + ... + dp[n-1][0]
이므로 dp[n][k] = dp[n][k-1] + dp[n-1][k] (k < n)

그러므로
dp[n][k] = dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n] if k >= n else 0 (n > 1)

리스트 두줄만 사용해서 메모리를 최적화 할 수 있다.
캐시와 재귀를 사용할 수도 있는데, 엄청 느리고 메모리도 많이 사용한다.

더 최적화된 풀이들은 마호니안 수를 이용하거나 누적합 배열을 이용한다.
지금은 여기서 멈춰야겠다...
"""
import inspect

# functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
sol = Solution()
functions = [member for member in inspect.getmembers(sol, predicate=inspect.ismethod)]
my_func = functions[0][1]
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
