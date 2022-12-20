# https://www.acmicpc.net/problem/14425
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
이전에 set를 이용해 간단하게 풀었던 문제다. 트라이를 공부하며 트라이로 다시 풀어봤다.
pypy 사용하지 않으면 시간초과.
"""

class Node:
    def __init__(self, key, data=None):
        self.key = key  # 무슨 글자인가
        self.data = data  # 단어가 끝났으면 데이터에 표기
        self.children = {}  # 자식 노드 가리키는 포인터. 딕셔너리로 구현

class Trie:
    def __init__(self):
        self.head = Node(None)  # 트라이 생성 시 헤드를 만들어줌

    def insert(self, string):
        cur_node = self.head  # 헤드부터 시작
        for char in string:  # 한 글자씩
            if char not in cur_node.children:  # 글자가 현재 노드 자식에 없으면 생성
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]  # 자식노드로 이동
        cur_node.data = string  # 단어 끝났으면 단어 기록

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:  # 글자가 현재 노드 자식에 있으면 자식노드로 이동
                cur_node = cur_node.children[char]
            else:  # 자식노드에 없으면 단어 없음.
                return False
        if cur_node.data != None:  # 글자는 있으나 단어기록 없으면 없는거임.
            return True

n_set, n_check = map(int, input().split())
s = Trie()
for _ in range(n_set):
    s.insert(input())
count = 0
for _ in range(n_check):
    if s.search(input()):  # 트라이에 단어 있으면 +1
        count += 1
print(count)
