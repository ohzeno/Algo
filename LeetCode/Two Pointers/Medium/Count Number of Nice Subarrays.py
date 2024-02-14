# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        num_odd = sub_nice = acc_nice = ll = 0
        for rr in range(len(nums)):
            if nums[rr] % 2 == 1:  # 홀수면
                num_odd += 1  # 홀수 갯수 증가
                sub_nice = 0  # 홀수가 나오면 매칭이 깨지므로 sub_nice 초기화
            while num_odd == k:  # 홀수가 k개인 동안 왼쪽 경우의 수 탐색
                sub_nice += 1
                if nums[ll] % 2 == 1:
                    num_odd -= 1
                ll += 1  # k개가 깨지도록 하기 때문에 이후 rr 순회에서 홀수가 안나오면 계속 sub_nice를 누적하게 된다.
            acc_nice += sub_nice  # 왼쪽 경우의 수 누적
        return acc_nice

inputdatas = [
    [[1,1,2,1,1], 3],
    [[2,4,6], 1],
    [[2,2,2,1,2,2,1,2,2,2], 2],
]

"""
LeetCode Medium. 투포인터나 슬라이딩 윈도우, 누적합이 연관된 문제라는 점을 알고도 풀지 못했다.
첫 LeetCode 문제인데 Medium이 생각보다 빡세다.
2중 for문을 사용하니 시간초과. 결국 투포인터 풀이를 보고 공부했다.
case3 같은 경우 0~3과 6~9가 모두 매칭되어야 하는데
투포인터를 사용하면 한쪽이 움직이는 순간 손실되는 경우의 수가 생긴다.
예를 들면 0, 6에서 3, 6으로 ll을 옮기면 0, 9를 탐색하지 못한다.
다른 사람의 풀이를 보니 0, 6에 도달하면 3, 6까지 경우의 수를 구해놓고
rr을 9까지 옮기면서 해당 경우의 수를 다 더해줬다.
그러면 0~3 4가지 x 6~9 4가지가 되어 모든 경우의 수를 검토할 수 있다.
(3, 6의 1, 1을 포함한 모든 케이스 탐색)
중간에 홀수가 또 나오면 갯수가 바뀌어서 매칭이 깨지므로 저장해둔 경우의 수를 초기화한다.
말로 설명하기 힘들어서 디버깅, 그림으로 이해해야 한다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for nums, k in inputdatas:
    print(functions[0][1](nums, k))
