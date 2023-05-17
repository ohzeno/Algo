# https://leetcode.com/problems/first-bad-version/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= bad <= n <= 2^31 - 1
"""
def isBadVersion(version: int) -> bool:
    if versions[version - 1] == 1:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ll, rr = 1, n
        while ll < rr:  # =을 넣으면 무한루프에 빠짐. 오름쪽 끝은 bad고 rr은 바뀌어도 항상 bad인데, ll == rr이 되면 ll의 값이 변하지 않기 때문.
            mid = (ll + rr) // 2
            if isBadVersion(mid):
                rr = mid  # rr은 항상 bad version
            else:
                ll = mid + 1  # 탈출은 항상 여기서 발생함. mid + 1이 rr이 됨. rr은 이미 검사했던 거니 탈출.
        return rr

inputdatas = [
    [5, [0, 0, 0, 1, 1]],
    [1, [1]]
]

"""
LeetCode Easy.
전형적인 이분탐색 문제.
isBadVersion() 함수가 릿코드 서버 내에 저장되어 있고, input값이나 bad가 int 하나씩으로만 주어져서
isBadVersion() 함수를 직접 구현하고, 서버와 똑같이 동작하도록 inputdatas도 새로 만들었다.
적어도 다른 문제처럼 api함수 코드랑 채점방식 수도코드라도 공개해주면 안되나...

bisect는 사용하지 못한다. 
bisect_left(반복 가능한 객체, 넣을 값, 시작 인덱스, 끝 인덱스)인데,
객체에 접근할 수 없기 때문.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    versions = t[1]
    print(my_func(t[0]))
