# https://leetcode.com/problems/subarray-sum-equals-k/description/
from typing import Optional, List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc_d = {0: 1}
        acc = cnt = 0
        for n in nums:
            acc += n
            cnt += acc_d.get(acc - k, 0)
            acc_d[acc] = acc_d.get(acc, 0) + 1
        return cnt


inputdatas = [
    {"data": [[1,1,1], 2], "answer": 2},
    {"data": [[1,2,3], 3], "answer": 2},
    {"data": [[-1,-1,1], 0], "answer": 1},
    {"data": [[-1,1,-1,1], 0], "answer": 4},
    {"data": [[0, 0, 0], 0], "answer": 6},
]

"""
LeetCode Medium.
제출 2.8M, 정답률 43.6%
이런 문제 전에도 풀었던 것 같은데 잘 기억나지 않는다.
Medium치고는 좀 어렵게 느껴졌다. 2중 for문을 사용하면 편하겠지만 시간복잡도가 너무 높아진다.

처음에 Counter를 사용하려다가, 부분집합이 아니라 하위배열이라 실패.
투포인터로 풀려 했는데, 음수가 있어서 포인터 이동 방향을 선택할 수 없었다.
누적합과 해시맵을 이용하면 편해지지만 직관적이지 않다.
hint4를 읽고 나면 좀 이해하기 편해진다.
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

0:1 을 추가하는 이유는 누적합 배열을 만들 때 초기화를 위해 필요한 작업이기 때문이다.
첫 원소가 k이면 acc-k가 0이 되고, cnt에 1을 더해야 하는데 0이 딕셔너리에 없기 때문.

이 때, 하위 배열은 비어있지 않아야 하는데, 
0:1을 넣어둬도 cnt에 더해지는 경우는 최소 한 개의 숫자를 선택한 후, acc가 k일 때 뿐이다.
즉, 비어있는 케이스는 cnt에 더해지지 않는다.

그럼 첫 원소가 0이고, k도 0인 경우는?
첫 원소를 체크할 때는 첫 원소만 들어간 케이스가 더해진다.
그리고 d[0]이 2가 될텐데, 이후에 이게 더해질 때는 
배열에 원소가 최소 한 개 들어가 있는 경우가 되기 때문에 상관없다.

nums = [0, 0, 0]을 생각해보면 
첫 0을 체크할 때는 d[0] = 1이라 정답에 1이 더해지는데,
[0] 하나이니 올바르다.
두번째 0을 체크할 때 d[0] = 2라 정답에 2가 더해지는데,
이는 [0, 0](idx 0, 1)과 [0](idx 1) 두 케이스가 더해지는 것이다. []는 더해지지 않는다.
세번째 0을 체크할 때 d[0] = 3이라 정답에 3이 더해지는데,
이는 [0, 0, 0], [0, 0](idx 1, 2), [0](idx 2) 세 케이스가 더해지는 것이다.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
