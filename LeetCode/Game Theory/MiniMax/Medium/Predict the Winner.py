# https://leetcode.com/problems/predict-the-winner/
from typing import Optional, List
from functools import cache

"""
constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
플레이어 1, 2가 0점으로 시작. 1이 먼저 시작
nums 처음 아니면 끝 원소를 선택. 선택한 원소는 nums에서 제거.
선택한 숫자를 점수에 더함. 원소 안남으면 끝.
1이 이기면 true 리턴. 점수 같으면 1이 이김.
두 플레이어는 최적의 선택을 한다고 가정.
"""


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def maxDiff(ll, rr):
            if ll == rr:
                return nums[ll]
            lp = nums[ll] - maxDiff(ll + 1, rr)
            rp = nums[rr] - maxDiff(ll, rr - 1)
            return max(lp, rp)

        return maxDiff(0, len(nums) - 1) >= 0


inputdatas = [
    [1, 5, 2],
    [1, 5, 233, 7],
]

"""
LeetCode Medium.
정답률 55.4%라는데 못풀어서 Editorial을 참고했다.
한 턴이 아니라 경기 전체에 있어 최적해를 선택해야 하기 때문에 
경기가 끝날 때까지의 진행을 고려해야 한다.
처음에는 points 배열과 turn 변수를 두고 풀었는데 꼬였다.

아무도 언급하지 않았지만 이는 게임이론의 MiniMax 알고리즘과 유사하다.

풀이1. 재귀
플레이어1과 플레이어 2의 점수 절대치는 경기 결과와 무관하다.
상대 점수만 알면 되므로 플레이어1의 점수에서 플레이어2의 점수를 뺀 diff가 경기 결과를 결정한다.
각 플레이어는 최적의 선택을 하므로 매 턴에서 maxDiff를 구해준다.
매 턴을 계산할 것이라 ll은 결국 rr과 같아진다. 그 때는 nums[ll]을 선택할 수 밖에 없다.
그 외의 경우에는 왼쪽, 오른쪽을 선택할 경우를 비교해야 한다.
왼쪽을 선택하고 나면 ll+1부터 rr까지가 남는다. 이 때 플레이어2가 최적의 선택을 하므로
maxDiff(ll+1, rr)은 플레이어 2의 최적해다. 하지만 이는 플레이어 1에게는 마이너스이므로
플레이어1이 ll을 선택했을 때의 점수는 nums[ll] - maxDiff(ll+1, rr)이다.
오른쪽을 선택할 경우에도 마찬가지다.
이 둘 중 최대값을 플레이어1이 선택하므로 maxDiff(ll, rr)을 리턴한다.
시작은 무조건 플레이어 1이므로 maxDiff(0, len(nums)-1)은 
플레이어 1이 최적선택을 했을 경우의 결과다.
이 값이 0보다 크거나 같으면 플레이어 1의 점수가 플레이어 2의 점수보다 크거나 같다는 뜻이므로 
플레이어 1이 이긴다.
ll, rr에 따라 결과값이 고정이므로 cache를 사용해 시간복잡도를 줄여준다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
