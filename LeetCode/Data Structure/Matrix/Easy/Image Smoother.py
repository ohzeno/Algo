# https://leetcode.com/problems/image-smoother/
from typing import Optional, List

"""
constraints:
  • m == img.length
  • n == img[i].length
  • 1 <= m, n <= 200
  • 0 <= img[i][j] <= 255
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        lr, lc = len(img), len(img[0])
        new_img = [[0] * lc for _ in range(lr)]
        for r in range(lr):
            for c in range(lc):
                cnt = acc = 0
                for r2 in range(r-1, r+2):
                    if not 0 <= r2 < lr:
                        continue
                    for c2 in range(c-1, c+2):
                        if 0 <= c2 < lc:
                            cnt += 1
                            acc += img[r2][c2]
                new_img[r][c] = acc//cnt
        return new_img


inputdatas = [
    {"data": [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]],
     "answer": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]},
    {"data": [[[100, 200, 100], [200, 50, 200], [100, 200, 100]]],
     "answer": [[137, 141, 137], [141, 138, 141], [137, 141, 137]]}
]

"""
LeetCode Easy.
제출 278.5K, 정답률 68.7%
코드가 더럽지만 가독성을 개선하면 실행시간이 늘고 디버깅이 힘들어진다.
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
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
