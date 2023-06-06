# https://leetcode.com/problems/erect-the-fence/
from typing import Optional, List
"""
1 <= trees.length <= 3000
trees[i].length == 2
0 <= xi, yi <= 100
All the given positions are unique.
"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def ccw(a, b, c):
            """
            Counter Clock Wise.
            v1: a -> b    v2: a -> c
            a -> b -> c의 회전 방향.
            v1과 v2의 외적의 z값이 양이면 좌회전, 음이면 우회전, 0이면 일직선.
            v1 X v2 =   |i   j   k|
                        |x1 y1  z1|
                        |x2 y2  z2|
            v1 X v2의 z값: x1 * y2 - x2 * y1
            """
            x1, y1 = b[0] - a[0], b[1] - a[1]
            x2, y2 = c[0] - a[0], c[1] - a[1]
            return x1 * y2 - x2 * y1
        trees.sort()  # Monotone Chain은 (x, y)순으로 정렬해야 한다.
        upper, lower = [], []
        for tree in trees:
            while len(lower) >= 2 and ccw(lower[-2], lower[-1], tree) < 0:  # 아래쪽은 좌회전이 필요하다. 우회전 요소 제거
                lower.pop()
            while len(upper) >= 2 and ccw(upper[-2], upper[-1], tree) > 0:  # 위쪽은 우회전이 필요하다. 좌회전 요소 제거
                upper.pop()
            lower.append(tuple(tree))
            upper.append(tuple(tree))
        return list(set(lower + upper))  # 중복 제거 후 리턴

inputdatas = [
    [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]],
    [[1,2],[2,2],[4,2]],
]

"""
LeetCode Hard.
한 8분 고민하다가 그냥 찾아보는게 빠르겠다 싶어서 찾아봤다.
Convex Hull 알고리즘(블록 껍질 알고리즘)이란게 존재했고, 
그 중에 Graham Scan, Andrew's Algorithm(Monotone Chain) 등등이 있었다.
frequency 3위의 Hard 문제에 내가 모르는 알고리즘이 나와서 당황스러웠는데, 
찾아보니 백준 플래티넘에 주로 나오는 알고리즘이다.
Monotone Chain 알고리즘을 사용했다. 외적을 오랜만에 봐서 반가웠다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
