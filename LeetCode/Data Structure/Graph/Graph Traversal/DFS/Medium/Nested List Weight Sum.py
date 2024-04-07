# https://leetcode.com/problems/nested-list-weight-sum/
from typing import Optional, List

"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

constraints:
1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is not None:
            self._integer = value
        else:
            self._integer = None
        self._list = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self._integer is not None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self._integer is not None:
            raise ValueError("This NestedInteger already holds a single integer.")
        self._list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        if self._integer is not None:
            raise ValueError("This NestedInteger already holds a single integer.")
        self._integer = value
        self._list = []

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self._integer

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self._list if self._list else None


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            res = 0
            for item in nestedList:
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    res += dfs(item.getList(), depth + 1)
            return res

        return dfs(nestedList, 1)


inputdatas = [
    {"data": [[[1, 1], 2, [1, 1]]], "answer": 10},
    {"data": [[1, [4, [6]]]], "answer": 27},
    {"data": [[0]], "answer": 0},
]

"""
LeetCode Medium.
제출 324.4K, 정답률 83.5%
문제 자체는 미디움 치고는 쉽다.
정작 문제 자체보다 인터페이스 구현과 빌더 만들기에 시간을 더 썼다.
인터페이스 설명과 실제 데이터가 충돌해서 데이터를 기반으로 작성했다.
"""


def buildNestedIntegerList(lst):
    """
    Given a nested list, builds a structure of NestedInteger objects and
    returns it as a list of NestedInteger at the top level.
    """

    def buildNestedInteger(lst):
        if isinstance(lst, int):  # 정수면 바로 인스턴스 생성
            return NestedInteger(lst)
        nested = NestedInteger()
        for item in lst:
            if isinstance(item, list):  # 리스트면 재귀 호출
                nested.add(buildNestedInteger(item))
            else:  # 정수면 바로 인스턴스 생성
                nested.add(NestedInteger(item))
        return nested

    return [buildNestedInteger(item) for item in lst]


import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    data = buildNestedIntegerList(data[0])
    res = my_func(sol, data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
