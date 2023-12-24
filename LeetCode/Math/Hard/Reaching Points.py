# https://leetcode.com/problems/reaching-points/
from typing import Optional, List

"""
constraints:
1 <= sx, sy, tx, ty <= 10^9

가능한 연산 결과: (x, x+y), (x+y, y)
연산으로 만들 수 있으면 True, 아니면 False 리턴.
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        연산 횟수를 줄이기 위해 역으로 연산한다.
        본래 연산은 (x, x+y), (x+y, y)이므로
        역 연산은 (tx, ty-tx), (tx-ty, ty)이다.
        그런데 마이너스 연산에서 음수가 나오면 안되므로
        tx > ty이면 tx -= ty만 가능하고
        tx < ty이면 ty -= tx만 가능하다.
        while문 조건 때문에 tx=ty는 존재하지 않으므로 체크해줄 필요 없다.
        -=연산을 축약해서 시간복잡도를 줄인 것인데,
        ty를 빼는 도중에 tx < ty가 되면 tx -= ty를 할 수 없다.
        그러므로 도중에 tx < ty가 될 수 없다는 것을 증명해야 한다.

        tx >= sx + ty
        tx - sx >= ty이므로
        (tx - sx) % ty에서 ty는 최소 1회 이상 뺀 것이다.
        나머지 연산의 특성 상 ty를 n회 뺐다고 하면
        n-1회는 n회 뺀 것에 비해 ty가 더해져 있으므로 ty보다 작을 수가 없다.
        """
        # 역연산 여지가 있는 동안
        while tx >= sx + ty or ty >= sy + tx:
            if tx > ty:
                # tx -= (tx - sx) // ty * ty
                tx = sx + (tx - sx) % ty
            else:
                # ty -= (ty - sy) // tx * tx
                ty = sy + (ty - sy) % tx
        return sx == tx and sy == ty


inputdatas = [
    [[1, 1, 3, 5], True],
    [[1, 1, 2, 2], False],
    [[1, 1, 1, 1], True],
    [[1, 1, 1000000000, 1], True],
    [[9, 10, 9, 19], True],
    [[9, 10, 9, 1], False],
    [[9, 10, 9, 11], False],
    [[10, 9, 19, 9], True],
]

"""
LeetCode Hard.
제출 180.5K, 정답률 32.8%
Editorial에 내 시간초과 풀이가 솔루션으로 올라가있다. 
시간초과 되는걸 풀이에 넣어놓으면 어떡해...

연산을 축약하는 형태의 풀이가 필요했고
축약 자체는 했으나 예외케이스를 처리할 방법이 생각나지 않았다.
결국 풀이들을 참고하여 최종 풀이를 작성했다.

풀이 자체는 어느정도 직관적으로 이해가 됐는데
수학적 증명이 어딜 찾아봐도 없어서 직접 증명했다.
또 다른 예외케이스가 두루뭉실하게 생각나서
예외를 명제로 구체화 하는데 시간을 한참 썼고,
명제를 증명하는 데에도 한참 썼다.
적어도 한 시간은 쓴듯.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for data, ans in inputdatas:
    if my_func(*data) == ans:
        print("pass")
    else:
        print("fail")
