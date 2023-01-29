# https://www.acmicpc.net/problem/10538
import sys, collections

sys.stdin = open('input.txt')


class Node:
    def __init__(self):
        self.children = [-1] * 2
        # valid가 false면 추가하지 않은 문자 혹은 중간 과정 때문에 생긴 문자
        # valid가 true면 추가한 문자
        self.valid = -1
        self.pi = -1

class Trie:
    def init(self):
        x = Node()
        self.trie.append(x)
        return len(self.trie) - 1

    def __init__(self):
        self.trie = []
        self.root = self.init()

    # node = 탐색하고 있는 노드의 인덱스
    # string = 추가하려고 하는 문자열
    # index = string의 몇번째 인덱스를 추가하려 하는가
    def add(self, node, string, index):
        if index == len(string):
            self.trie[node].valid = node
            return node
        c = 1 if string[index] == 'o' else 0
        if self.trie[node].children[c] == -1:
            next = self.init()
            self.trie[node].children[c] = next
        child = self.trie[node].children[c]
        return self.add(child, string, index + 1)

    def search(self, string):
        root = self.root
        trie = self.trie
        n = len(string)
        ans = [-1] * n
        node = root
        for i in range(n):
            node = self.aho_corasick(node, string[i])
            ans[i] = trie[node].valid
        return ans

    def aho_corasick_failure(self):
        trie = self.trie
        root = self.root
        q = collections.deque()
        trie[root].pi = root
        q.append(root)
        while q:
            cur = q.popleft()
            for i in range(2):
                next = trie[cur].children[i]
                if next == -1:
                    continue
                if cur == root:
                    trie[next].pi = root
                else:
                    x = trie[cur].pi
                    while x != root and trie[x].children[i] == -1:
                        x = trie[x].pi
                    if trie[x].children[i] != -1:
                        x = trie[x].children[i]
                    trie[next].pi = x
                pi = trie[next].pi
                q.append(next)

    def aho_corasick(self, node, char):
        trie = self.trie
        root = self.root
        c = 1 if char == 'o' else 0
        while node != root and trie[node].children[c] == -1:
            node = trie[node].pi
        if trie[node].children[c] != -1:
            node = trie[node].children[c]
        return node

def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    # 첫번째 수의 fail 값은 0
    for i in range(1, len(pattern)):
        # 만일 지금까지 매칭이 된 글자와 새로운 글자가 같지 않으면
        # 그전에 어디까지 매칭되었는지에 따라 조정이 필요하니까
        # j는 j 한칸 앞의 fail로 나타낸다
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
        else:
            table[i] = 0
    return table

def kmp(parent, pattern, pi):
    ans = 0
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = pi[j - 1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                ans += 1
                j = pi[j]
            else:
                j += 1
    return ans


hsmall, wsmall, hbig, wbig = map(int, sys.stdin.readline().split())
my = Trie()
small = [sys.stdin.readline().rstrip() for _ in range(hsmall)]
big = [sys.stdin.readline().rstrip() for _ in range(hbig)]
p = []
for i in range(hsmall):
    p.append(my.add(my.root, small[i], 0))
my.aho_corasick_failure()
d = []
for i in range(hbig):
    d.append(my.search(big[i]))
pi = failure(p)
ans = 0
for j in range(wsmall - 1, wbig):
    s = [0] * hbig
    for i in range(hbig):
        s[i] = d[i][j]
    ans += kmp(s, p, pi)
print(ans)