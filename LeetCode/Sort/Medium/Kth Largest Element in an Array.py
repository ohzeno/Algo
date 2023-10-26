# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import Optional, List

"""
constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from random import choice
from heapq import heappop, heapify
from collections import Counter


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 퀵셀렉트
        # def partition(arr, pivot):
        #     smaller, mid, bigger = [], [], []
        #     for num in arr:
        #         if num < pivot:
        #             smaller.append(num)
        #         elif num > pivot:
        #             bigger.append(num)
        #         else:
        #             mid.append(num)
        #     return smaller, mid, bigger
        #
        # def quick_select(arr, k):
        #     pivot = choice(arr)
        #     smaller, mid, bigger = partition(arr, pivot)
        #     len_s, len_m, len_b = len(smaller), len(mid), len(bigger)
        #     if k <= len_b:
        #         return quick_select(bigger, k)
        #     elif len_m < k - len_b:
        #         return quick_select(smaller, k - len_b - len_m)
        #     return pivot
        #
        # return quick_select(nums, k)
        # 2. 정렬
        # return sorted(nums, reverse=True)[k-1]
        # 3. 우선순위 큐
        # heapify(nums)
        # for _ in range(len(nums) - k):
        #     heappop(nums)
        # return heappop(nums)
        # 4. 카운팅 정렬
        """
        Counter를 사용할까 했는데, 그러면 counts의 인덱스를 역순으로 순회하는 부분에서 결국
        Counter의 키값을 역순 정렬해서 순회해야 한다.
        """
        min_num, max_num = min(nums), max(nums)
        counts = [0] * (max_num - min_num + 1)
        for num in nums:
            counts[num - min_num] += 1
        remain = k
        for num in range(len(counts) - 1, -1, -1):
            remain -= counts[num]
            if remain <= 0:
                return num + min_num


inputdatas = [
    [[[1, 2, 2, 2, 2, 3], 1], 3],
    [[[1, 2, 2, 2, 2, 3], 2], 2],
    [[[1, 2, 2, 2, 2, 3], 3], 2],
    [[[1, 2, 2, 2, 2, 3], 4], 2],
    [[[1, 2, 2, 2, 2, 3], 5], 2],
    [[[1, 2, 2, 2, 2, 3], 6], 1],
    [[[3, 2, 1, 5, 6, 4], 2], 5],
    [[[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], 4],
]

"""
LeetCode Medium.
제출 3M, 정답률 67.0%
kth largest이지만 distinct와 다르다고 해서 당황했다.
k번째 큰 수는 당연히 distinct로 세는게 아닌가?
그런데 문제에서는 다른 표현을 사용하지 않고
'Note that it is the kth largest element in the sorted order, 
not the kth distinct element.'
라고 했다. 그래서 영어권에서 일상용어로 k번째라는 표현을 사용할 때 중복도 세나 했는데
유학파 몇 명한테 물어보니 중복을 안세는게 정상이라고 한다.
ex) 3, 2, 2, 1에서 3번째 큰 수를 찾으라고 하면
문제: 2
일상: 1 (2번째 큰 수가 둘인 것이지 3번째 큰 수가 2인 것이 아니다)
그나마 이 문제에선는 의미를 명시해놨는데, 
저번 모 회사 시험처럼 문장이 이상하면 문제를 잘못 이해할 수 있을 듯 하다.
코딩 하는 사람들이면 좀 논리적으로 명확한 문장을 적어줬으면 좋겠다.

정렬 없이 풀라고 되어있어서 정렬 안쓰고 풀려다가 포기했다.
정작 정렬을 사용한 한줄 풀이가 정답처리된다...
그리고 우선순위큐도 결국 정렬을 이용하는 것인데...
퀵셀렉트를 처음 봤다. 이것도 일종의 정렬인 것 같긴 한데...
평범한 퀵셀렉트로 풀 수 있다고 주장하는 파이썬 풀이들이 여럿 올라와 있었으나 모두 시간초과다.
물론 내가 작성한 퀵셀렉트 풀이도 시간초과 발생.
퀵셀렉트로 통과하려면 정석으로는 안되고 변형 풀이를 사용해야 한다.

Editorial에선 퀵셀렉트도 아예 새 배열을 만들고, 
중복때문에 애매한 중간값도 새 배열로 만들어버려서 간단하게 해결한다.

카운팅 정렬도 처음 배웠다.
비교 없이 정렬한다길래 어떤 건가 했는데, 정확히는 원본 배열은 정렬하지 않고 
카운팅 배열을 만들어서 idx를 순회하면 정렬과 같은 효과가 생긴다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for data, ans in inputdatas:
    res = my_func(*data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
