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


class BrowserHistory:
    def __init__(self, homepage: str):
        self.url = homepage
        self.back_history = []
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.back_history.append(self.url)
        self.forward_history = []
        self.url = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.back_history:
                break
            self.forward_history.append(self.url)
            self.url = self.back_history.pop()
        return self.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.forward_history:
                break
            self.back_history.append(self.url)
            self.url = self.forward_history.pop()
        return self.url


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

2개의 스택으로 풀어봤다.
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
