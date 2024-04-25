# https://leetcode.com/problems/random-pick-with-weight/
from typing import Optional, List

"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

constraints:
1 <= w.length <= 10^4
1 <= w[i] <= 10^5
pickIndex will be called at most 10^4 times.
"""

from itertools import accumulate
import random
from bisect import bisect_left as bl

class Solution:
    def __init__(self, w: List[int]):
        self.prefixSum = list(accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefixSum[-1])
        return bl(self.prefixSum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


inputdatas = [
    {
        "data": [["Solution", "pickIndex"], [[[1]], []]],
    },
    {
        "data": [
            [
                "Solution",
                "pickIndex",
                "pickIndex",
                "pickIndex",
                "pickIndex",
                "pickIndex",
            ],
            [[[1, 3]], [], [], [], [], []],
        ],
    },
]

"""
LeetCode Medium.
제출 954.2K, 정답률 46.8%
각 가중치만큼의 확률로 인덱스가 선택되도록 하는 문제.
누적합을 이용하는 방법을 사용했다. 
예전에 사용했던 방법인지는 모르겠으나 기억나지 않았다.

누접합을 이용해 가중치만큼의 숫자 분포를 만드는게 핵심이다.
예를 들어 원래 값이 1, 2, 3이라면 세 수는 1이라는 값이 겹친다. 2와 3은 2가 겹치고.
하지만 누적합으로 1, 3, 6을 만들면 1, 2~3, 4~6로 나누어지고, 각 구간의 수의 갯수가 가중치와 같아진다.
그럼 전체에서 랜덤으로 숫자를 뽑으면 가중치 만큼의 확률로 구간이 선택된다.
"""


def grading(orders, ws):
    res = []
    for order in orders:
        if order == "Solution":
            res.append(None)
            w_data = ws.pop(0)
            if len(w_data) == 1:
                obj = Solution(w_data[0])
            else:
                obj = Solution(w_data)
        else:
            res.append(obj.pickIndex())
    return res

for inputdata in inputdatas:
    data = inputdata["data"]
    res = grading(*data)
    print(res)
    # if res == ans:
    #     print("pass")
    # else:
    #     summary = "fail"
    #     for label, content in [("expected:", ans), ("got:", res)]:
    #         summary += f"\n  {label}\n"
    #         summary += f"    {content}\n"
    #         summary = summary.rstrip()
    #     print(summary)
