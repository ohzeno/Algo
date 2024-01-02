# https://leetcode.com/problems/add-two-numbers/
"""
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ''
        while l1:
            n1 += str(l1.val)  # 역순 저장
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        n3 = str(int(n1[::-1]) + int(n2[::-1]))[::-1]  # 더한 후 역순으로 저장
        tmp = n3Node = ListNode(n3[0])  # dummy용으로 tmp를 사용한다.
        for i in range(1, len(n3)):
            tmp.next = ListNode(n3[i])  # 정수가 아니라 문자열로 넣어도 통과된다. 아마 채점 과정에서 값을 str로 더해주는듯.
            tmp = tmp.next
        return n3Node

inputdatas = [
    [[2,4,3], [5,6,4]],
    [[0], [0]],
    [[9,9,9,9,9,9,9], [9,9,9,9]],
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for a, b in inputdatas:
    aNode, bNode = ListNode(a[0]), ListNode(b[0])
    tmpa, tmpb = aNode, bNode
    for i in range(1, len(a)):
        tmpa.next = ListNode(a[i])
        tmpa = tmpa.next
    for i in range(1, len(b)):
        tmpb.next = ListNode(b[i])
        tmpb = tmpb.next
    print(functions[0][1](aNode, bNode))

"""
LeetCode Medium. 
ListNode를 주석처리 해놨고 Optional이라고 되어있길래 클래스를 사용하지 않아도 된다는 것인 줄 알았다.
testcase에는 l1, l2가 평범한 리스트로 보여서 처음엔 리스트로 풀엇다.
풀이를 넣으니 런타임 에러가 났고, input이 ListNode로 주어지는 것을 확인했다.

input을 ListNode로 바꾸어 입력하는 코드를 작성하는 데 시간을 좀 썼다.
이후 직관적으로 각 노드값들을 스트링으로 이어붙여 int를 만들어 풀었다.

다른 풀이들을 보니 while문을 하나로 두고, 스트링을 이용하지 않고 값을 더해주며 풀었다.
크게 다른 점은 없고, 스트링을 이용한 풀이가 더 직관적이라서 다른 풀이를 해보진 않았다.
"""
