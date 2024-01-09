# https://leetcode.com/problems/tallest-billboard/
from typing import Optional, List

"""
용접할 수 있는 막대 목록 rods가 주어진다.
1, 2, 3 막대가 있으면 용접으로 6으로 만들 수 있음.
용접으로 두 막대를 같은 높이로 만들 수 있는 최대 높이를 반환하라.
불가능하면 0을 반환.

constraints:
1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods) <= 5000
"""


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # diff: smaller
        dp = {0: 0}  # 차이 없는 케이스
        for new_rod in rods:
            # 기존 막대들에 추가
            for diff, smaller in list(dp.items()):
                # 큰 막대에 추가
                d1 = diff + new_rod  # 새로운 diff
                dp[d1] = max(dp.get(d1, 0), smaller)
                # 작은 막대에 추가
                d2 = abs(new_rod - diff)  # 새로운 diff
                dp[d2] = max(
                    dp.get(d2, 0),
                    # 1. new_rod > diff: taller(smaller + diff)
                    # 2. new_rod < diff: smaller + new_rod
                    smaller + min(diff, new_rod),
                )
        return dp[0]


inputdatas = [
    [[1, 2, 3, 6], 6],
    [[1, 2, 3, 4, 5, 6], 10],
    [[1, 2], 0],
    [[1, 1, 1, 1, 1, 5], 5],
]

"""
LeetCode Hard.
제출 108.3K, 정답률 52.5%

못풀어서 Editorial과 Submissions를 참고했다.
비슷한 문제가 올림피아드에 출제된 적 있고, 고난이도 문제였다고 한다.
그런데 이게 왜 자주 출제되는 문제에...?

베스트 풀이들의 해설은 Editorial을 이해한 후에 봐야 이해가 되도록 작성되어 있었다.
Editorial이 길어서 오랜만에 영어 많이 읽었다.

모든 케이스들을 살펴보면 시간복잡도가 크므로 dp를 이용한다.
dp[diff] = smaller: diff 차이의 막대들로 만들 수 있는 케이스중 작은쪽 막대의 최대 크기
dp[0] = 0: diff가 0인 케이스의 초기값은 0이다.
새로운 막대에 대해 기존 케이스들을 순회하며 
큰 막대에 추가하는 경우, 작은 막대에 추가하는 경우를 고려하여 업데이트 한다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
