# https://www.acmicpc.net/problem/14725
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
로봇 개미는 개미굴 각 층에 먹이가 있는 방을 따라 내려가다 더 내려갈 수 없으면 신호를 보낸다.
이 신호로 내려오며 알게된 각 방에 저장된 먹이 정보를 전달한다.
로봇 개미의 수는 각 개미굴 저장소를 모두 확인할 수 있을 만큼 넣는다.
각 층은 --로 구분한다.
같은 층에 여러 방이 있으면 사전 순서가 앞서는 먹이 정보가 먼저 출력된다.
첫 줄에 정보를 보내온 개미의 수 n(1~1000)개가 주어진다.
다음 n줄에는 각 개미가 보낸 먹이 정보 수 k, k개의 먹이 정보가 주어진다.
먹이 이름 길이는 1~15
개미굴의 시각화된 구조를 출력하라.
"""
class Node:
    def __init__(self, name):
        self.name = name
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, foods):
        cur = self.root
        for food in foods:
            cur = cur.child.setdefault(food, Node(food))

    def dfs(self, cur, depth):
        if cur.name:  # root 제외
            print('--' * depth + cur.name)  # 층 구분
        for p, child in sorted(cur.child.items()):
            self.dfs(child, depth + 1)

trie = Trie()
for _ in range(int(input())):
    info = input().split()[1:]
    trie.insert(info)
trie.dfs(trie.root, -1)  # root의 자식이 0이 되어야 하므로 -1

"""
현 시점 골드3. 제출 4688, 정답률 66.244%
오랜만의 트라이 문제. 역시 아직 어색하다.
"""