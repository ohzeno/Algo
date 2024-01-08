# https://leetcode.com/problems/make-array-strictly-increasing/
from typing import Optional, List

"""
정수배열 arr1, arr2가 주어진다.
arr1가 엄격한 오름차순이 되게 만들기 위한 최소 작업 횟수를 반환하라.

한 번의 작업에서 arr1의 한 원소를 arr2의 원소로 바꿀 수 있다.
만들 수 없으면 -1을 반환하라.

constraints:
1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""

from bisect import bisect_right as br


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        #     arr2 = sorted(set(arr2))
        #     len1, len2 = len(arr1), len(arr2)
        #     dp = {}
        #
        #     # arr[i1:]을 엄격한 오름차순으로 만들기 위한 최소 작업 횟수를 반환한다.
        #     def dfs(i1, prev):
        #         if i1 == len1:
        #             return 0
        #         if (i1, prev) in dp:
        #             return dp[(i1, prev)]
        #         cost = float("inf")
        #         if prev < arr1[i1]:
        #             # 이미 오름차순이면 그냥 냅둘 수 있음.
        #             cost = dfs(i1 + 1, arr1[i1])
        #         i2 = br(arr2, prev)
        #         if i2 < len2:
        #             # arr2[i2]로 바꾸는 경우
        #             cost = min(cost, 1 + dfs(i1 + 1, arr2[i2]))
        #         dp[(i1, prev)] = cost
        #         return cost
        #
        #     ans = dfs(0, -1)
        #     # 배열 자체보다 더 많이 바꾸는건 불가능.
        #     return ans if ans <= len1 else -1
        dp = {-1: 0}  # dp[이전 원소] = 최소 작업 횟수
        arr2.sort()
        for num in arr1:
            new_dp = {}
            for prev, ops in dp.items():
                if prev < num:  # 이미 오름차순이면 그냥 냅두는 것과 비교
                    new_dp[num] = min(new_dp.get(num, float("inf")), ops)
                i2 = br(arr2, prev)
                if i2 < len(arr2):
                    new_dp[arr2[i2]] = min(new_dp.get(arr2[i2], float("inf")), ops + 1)
            dp = new_dp
        return min(dp.values()) if dp else -1


inputdatas = [
    [[[1, 5, 3, 6, 7], [1, 3, 2, 4]], 1],
    [[[1, 5, 3, 6, 7], [4, 3, 1]], 2],
    [[[1, 5, 3, 6, 7], [1, 6, 3, 3]], -1],
    [
        [
            [13, 2, 17, 2, 1, 8, 7, 10, 3, 12, 7, 20, 13],
            [
                25,
                16,
                17,
                10,
                25,
                18,
                13,
                8,
                3,
                22,
                1,
                20,
                13,
                18,
                25,
                20,
                11,
                18,
                15,
                12,
            ],
        ],
        11,
    ],
]

"""
LeetCode Hard.
제출 94.8K, 정답률 58.6%

1시간동안 못풀어서 Editorial의 일부를 참고해서 답안을 작성했었으나,
시간초과를 해결하니 메모리 초과를 해결하지 못했다.
Editorial이 dp딕셔너리를 이용해 그걸 해결한다.
Solutions 베스트 답변이 훨씬 효육적이라 둘 다 공부했다.

원래 Editorial 아이디어는
arr2는 정렬해두고
arr1을 왼쪽부터 dfs하면서 이전 원소보다 크면
1. 그냥 냅두고 다음 원소로
2. arr2에서 이전 원소보다 큰 원소를 찾아서(이분탐색) 바꾸고 다음 원소로
두 가지를 모두 시행해보고
이전 원소보다 작거나 같으면 무조건 바꿔야 하니 2를 진행한다.
dfs과정에서 딕셔너리를 이용해 가지치기를 한다.

solutions 베스트 답변은
dp[이전 원소] = 최소 작업 횟수로 정의하고
arr1을 왼쪽부터 순회하면서
dp배열에서 prev들을 확인하며 작업을 진행한다.
매번 min작업을 통해 최소 작업 횟수를 갱신한다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(*data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
