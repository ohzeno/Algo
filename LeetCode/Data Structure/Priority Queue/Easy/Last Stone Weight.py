# https://leetcode.com/problems/last-stone-weight/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
from bisect import insort
from heapq import heapify, heappop as hpop, heappush as hpush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # leng = len(stones)
        # while leng > 1:
        #     stones.sort()
        #     if stones[-1] == stones[-2]:
        #         stones.pop()
        #         stones.pop()
        #         leng -= 2
        #     else:
        #         stones[-2] = stones[-1] - stones[-2]
        #         stones.pop()
        #         leng -= 1
        # return stones[0] if leng else 0
        # stones.sort()
        # leng = len(stones)
        # while leng > 1:
        #     max1, max2 = stones.pop(), stones.pop()
        #     if max1 == max2:
        #         leng -= 2
        #     else:
        #         insort(stones, max1 - max2)  # insort는 삽입해도 정렬을 유지해준다.
        #         leng -= 1
        # return stones[0] if leng else 0
        stones = list(map(lambda x: -x, stones))  # 최대 힙 만들려면 -로 넣어야함.
        leng = len(stones)
        heapify(stones)
        while leng > 1:
            max1, max2 = hpop(stones), hpop(stones)
            if max1 == max2:
                leng -= 2
            else:
                hpush(stones, max1 - max2)
                leng -= 1
        return -stones[0] if leng else 0


inputdatas = [
    [2,7,4,1,8,1],
    [1],
]

"""
LeetCode Easy.
처음엔 그냥 sort로 풀었고
heap 카테고리에 나온거라 heapq 사용방법을 찾아보다가 insort를 알게됐다.
insort는 정렬이 유지된 상태에서 삽입을 해준다.
heapq, insort, sort 세가지 방법을 전부 사용해봤다.
기존 insort, heapq 사용방법들은 전부 코드 간소화에만 집중했고, 항상 max1-max2를 삽입했다.
그래서 0이 여럿 들어간 상태로 계속 while문이 작동했다.
나는 직관적으로 알아볼 수 있게 max1, max2를 따로 만들고 if문을 사용했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
