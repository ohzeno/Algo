# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
from typing import Optional, List

"""
constraints:
1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100

정원은 0부터 n까지.
0~n까지 n+1 수도꼭지 존재.
ranges[i]는 i번째 수도꼭지의 범위.
[i - ranges[i], i + ranges[i]] 범위에 물을 줄 수 있음.
정원 전체에 물을 주기 위해 열어야 하는 최소 수도꼭지 수를 리턴.
불가하면 -1 리턴.
"""
from heapq import heappush as hpush, heappop as hpop


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # taps = {}
        # for i, v in enumerate(ranges):
        #     if v == 0:
        #         continue
        #     ll, rr = max(i-v, 0), min(i+v, n)
        #     taps.setdefault(ll, [])
        #     hpush(taps[ll], [ll-rr, rr])
        # if not taps or 0 not in taps:
        #     return -1
        # cnt = 1
        # re = taps[0][0][1]
        # tks = sorted(taps.keys())
        # l_taps = len(tks)
        # if l_taps == 1 and re < n:
        #     return -1
        # ni = 1
        # while re < n:
        #     candies = [0, re]
        #     while ni < l_taps and tks[ni] <= re:
        #         if taps[tks[ni]][0][1] > candies[1]:
        #             candies = taps[tks[ni]][0]
        #         ni += 1
        #     if not candies[0]:
        #         return -1
        #     re = candies[1]
        #     cnt += 1
        # return cnt
        rrs = [0]  # 비교 위해 0 넣어줌.
        for i, d in enumerate(ranges):
            ll, rr = i - d, min(n, i + d)
            # rr이 이전과 같아도 더 많은 범위 커버하는 경우는?
            # i가 증가하므로 rr이 같으면 더 많은 범위 커버하는 경우는 없다.
            # ll은 이전 끝보다 작거나 같아야 하고 rr은 더 커야 의미있음.
            if not (ll <= rrs[-1] < rr):
                continue
            # 2개 이상 있을 때 -2의 rr보다 ll이 작거나 같으면 -1 필요없음.
            while len(rrs) > 1 and ll <= rrs[-2]:
                rrs.pop()
            rrs.append(rr)
            if rr >= n:
                break
        if rrs[-1] < n:
            return -1
        return len(rrs) - 1  # 처음에 넣은 0 제외


inputdatas = [
    [5, [3, 4, 1, 1, 0, 0]],  # 1
    [3, [0, 0, 0, 0]],  # -1
    [9, [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]],  # 2
]

"""
LeetCode Hard.
제출 230.2K, 정답률 51.6%
초안은 46분 걸렸다. 얼마전에 푼 철로 문제와 비슷하지만 풀이가 다르다.
그 문제는 철로 범위에 선분이 가장 많이 들어오는 케이스를 찾는 것이었고
이번은 가든 범위에 선분이 가장 적게 들어오는 케이스를 찾아야 한다.

0에서 출발하는 탭부터 시작하고 범위가 가장 넓은 녀석을 선택했다.
이후 범위의 왼쪽 끝을 ll이라 하면 다음 ll부터 현재 커버 범위의 오른쪽 끝까지의 ll을 돌면서
첫 원소(범위 길이로 정렬해뒀으니 0번 인덱스만 가져오면 됨) 중에 
범위 우측 끝이 가장 긴 녀석을 선택했다.
커버 범위의 우측 끝을 업데이트하고 카운트를 1 올렸다.
시작점이 현 커버범위 이내이면서 커버 범위의 우측 끝이 가장 긴 녀석을 계속 선택해 나간다.

다른 풀이를 보고 새로 풀어봤다.
한 번의 순회 내에서 while문을 사용하여 훨씬 간단해졌고 더 빨라졌다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(*t))
