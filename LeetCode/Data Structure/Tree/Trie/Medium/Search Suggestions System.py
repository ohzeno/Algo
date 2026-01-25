# https://leetcode.com/problems/search-suggestions-system/
from typing import Optional, List

"""
constraints:
  • 1 <= products.length <= 1000
  • 1 <= products[i].length <= 3000
  • 1 <= sum(products[i].length) <= 2 * 10^4
  • All the strings of products are unique.
  • products[i] consists of lowercase English letters.
  • 1 <= searchWord.length <= 1000
  • searchWord consists of lowercase English letters.
"""

class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, product):
        cur = self.root
        for c in product:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            if len(cur.suggestions) < 3:
                cur.suggestions.append(product)

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        result = []
        cur = trie.root
        for c in searchWord:
            if cur and c in cur.children:
                cur = cur.children[c]
                result.append(cur.suggestions)
            else:
                cur = None
                result.append([])
        return result


inputdatas = [
    {"data": [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],
     "answer": [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
                ["mouse", "mousepad"], ["mouse", "mousepad"]]},
    {"data": [["havana"], "havana"], "answer": [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]},
    {"data": [["havana"], "tatiana"], "answer": [[], [], [], [], [], [], []]}
]

"""
LeetCode Medium.
제출 657.6K, 정답률 65.1%
처음엔 heapq를 썼는데 그냥 products 정렬하고 시작하면 된다.
문제 조건엔 searchWord와 매칭되는 단어가 없는 케이스의 대응을 명시하지 않았는데
제출해보면 예시에 3번 케이스가 있다.
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
