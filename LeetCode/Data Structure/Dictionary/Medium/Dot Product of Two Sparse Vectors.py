# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
from typing import Optional, List

"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            if num:
                self.vector[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in set(self.vector) & set(vec.vector):
            res += self.vector[i] * vec.vector[i]
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

inputdatas = [
    {"data": [[1,0,0,2,3], [0,3,0,4,0]], "answer": 8},
    {"data": [[0,1,0,0,0], [0,0,0,0,2]], "answer": 0},
    {"data": [[0,1,0,0,2,0,0], [1,0,0,0,3,0,4]], "answer": 6},
]

"""
LeetCode Medium.
제출 268.9K, 정답률 89.9%
첫 제출때 썼던 로직이 제일 빨랐다. dict나 set 좀 알면 쉬운 문제.
set로 key가 겹치는 경우만 구해서 계산했다.
다른 방법으로는 자신의 key만 순회하며 get(k, 0)으로 다른 벡터 값을 가져와도 된다.

더 빠른 방법이 하나 있긴 한데, numpy를 사용해야 한다.
제출기록을 보면 더 빠른 코드들이 많지만, 지금 제출해보면 내 코드보다 느리거나 비슷하다.
"""
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    nums1, nums2 = data
    v1, v2 = map(SparseVector, data)
    res = v1.dotProduct(v2)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
