# https://leetcode.com/problems/design-browser-history/
from typing import Optional, List

"""
constraints:
  • 1 <= homepage.length <= 20
  • 1 <= url.length <= 20
  • 1 <= steps <= 100
  • homepage and url consist of '.' or lower case English letters.
  • At most 5000 calls will be made to visit, back, and forward.
"""


class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.head.next = node
        node.prev = self.head
        self.head = node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.head.prev:
                self.head = self.head.prev
        return self.head.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.head.next:
                self.head = self.head.next
        return self.head.url


inputdatas = [
    {
        'input': {
            'cmds': ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back",
                     "back"],
            'url_or_n': [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1],
                         ["linkedin.com"], [2], [2], [
                             7]]
        },
        'answer': [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com",
                   "google.com", "leetcode.com"]
    }
]

"""
LeetCode Medium.
제출 357.8K, 정답률 78.0%

링크드 리스트 공부 예제로 받은 문제인데, 스택풀이가 훨씬 편할 듯 하다.
일단 visit때 버리는 노드체인에 대한 메모리 누수 문제가 있다. 
그렇다고 그거 다 지워주기엔 시간복잡도가 올라간다.
실제로 문제 설명도 스택을 전제해서 forward history를 비우라는 말이 있다.
"""


def grading(res, ans):
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)


for inputdata in inputdatas:
    cmds, url_or_n = inputdata['input']['cmds'], inputdata['input']['url_or_n']
    answer = inputdata['answer']
    obj = BrowserHistory(*url_or_n[0])
    for cmd, u, ans in zip(cmds[1:], url_or_n[1:], answer[1:]):
        if cmd == 'visit':
            res = obj.visit(*u)
        elif cmd == 'back':
            res = obj.back(*u)
        elif cmd == 'forward':
            res = obj.forward(*u)
        grading(res, ans)
