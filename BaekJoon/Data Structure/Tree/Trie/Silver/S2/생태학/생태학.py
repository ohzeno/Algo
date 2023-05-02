# https://www.acmicpc.net/problem/4358
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.count = 0  # data 카운트 위한 속성
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        if cur_node.data != string:
            cur_node.data = string
        cur_node.count += 1  # 단어 몇 번 들어왔는지 카운팅

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        if cur_node.data != None:
            return cur_node.count  # 단어 입력 횟수 반환

trie = Trie()
count = 0
trees = set()  # 사전순 출력 위한 세트
while True:
    data = input()
    if data == '':
        break
    else:
        trie.insert(data)
        trees.add(data)  # 중복 제거
        count += 1  # 총 단어 수
trees = sorted(list(trees))  # 사전순 리스트
for tree in trees:  # 사전 순으로
    # round(0.5)는 0으로 나옴. round연산의 문제점이기에 .4f로 반올림.
    print(f'{tree} {trie.search(tree)/count * 100:.4f}')