# https://www.acmicpc.net/problem/5639
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5 + 10)
"""
이진탐색트리 전위 순회 결과가 주어졌을 때 후위 순회 결과를 구하라.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data)

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        cur = self.root
        while True:
            if data < cur.data:
                if not cur.left:
                    cur.left = Node(data)
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = Node(data)
                    break
                else:
                    cur = cur.right

bst = binarySearchTree()
while True:
    try:
        bst.insert(int(input()))
    except:
        break
postorder(bst.root)



"""
현 시점 골드 5. 제출 40361. 정답률 38.253 %
이진 탐색 트리 순회 문제.
나는 트리를 직접 만들어서 풀었다.
베스트 풀이들을 보니 트리를 만들지 않고
스택을 이용하거나 인덱싱을 이용하거나 서브트리 탐색을 이용하여 풀었다.
그냥 직관적으로 트리를 직접 만드는게 코테 치르는 입장에서 최적해인 것 같다.
"""