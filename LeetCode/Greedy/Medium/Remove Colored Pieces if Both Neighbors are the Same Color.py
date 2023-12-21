# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
from typing import Optional, List
"""
n피스가 일렬로 놓여있음. 각 피스는 A, B 중 하나의 색.
앨리스, 밥이 번갈아가며 피스를 제거.
앨리스가 먼저 시작.
앨리스는 양 옆 피스가 A인 A만 제거 가능.
밥은 양 옆 피스가 B인 B만 제거 가능.
제거할 수 없는 상황이 오면 패배.
앨리스와 밥은 최적의 전략을 취한다고 가정할 때,
앨리스가 이기면 true, 밥이 이기면 false 리턴.

constraints:
1 <= colors.length <= 10^5
colors consists of only the letters 'A' and 'B'
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        nA = nB = 0
        for i in range(len(colors)-2):
            part = colors[i:i+3]
            if part == 'AAA':
                nA += 1
            elif part == 'BBB':
                nB += 1
        return nA > nB

inputdatas = [
    ['AAABABB', True],
    ['AA', False],
    ['ABBBBBBBAAA', False],
]

"""
LeetCode Hard.
제출 209K, 정답률 62.9%
각 플레이어가 최적해 찾는다고 해서 dp가 생각났는데 함정이었다.
단순히 A, B가 연속으로 3개 나오는 경우를 세면 되는 문제였다.
3개짜리 글자에서 안쪽만 가져갈 수 있어서 분리된 그룹을 셀 필요도 없다.
단순히 3개 이상 이어진 글자에서 안쪽 글자 갯수가 최종적으로 선택할 수 있는 갯수.
앨리스가 먼저 시작하므로 앨리스가 이기려면 갯수가 같은게 아니라 더 많아야 한다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, ans in inputdatas:
    res = my_func(data)
    if res == ans:
        print('pass')
    else:
        print('fail\n', f'expected:{ans}\n', f'got:{res}\n')
