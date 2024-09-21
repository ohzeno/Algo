# https://school.programmers.co.kr/learn/courses/30/lessons/17685
class Node:
    def __init__(self, string):
        self.string = string  # 현재 글자
        self.count = 0  # 몇 개의 단어가 이 지점을 포함하는가?
        self.child = {}  # 자식 노드

class Trie:
    def __init__(self):
        self.head = Node(None)  # 트라이 생성 시 헤드노드 만들어줌.

    def insert(self, word):
        cur = self.head
        for w in word:
            # w가 키에 있으면 value 반환, 없으면 Node(w) 설정 후 반환.
            cur = cur.child.setdefault(w, Node(w))
            cur.count += 1  # 현 지점 포함하는 단어 수 갱신

    def search(self, word):
        cur = self.head
        s = ''
        for idx, w in enumerate(word, 1):  # idx(찾아본 글자 수) 1부터 시작.
            # 이미 모든 단어가 학습됐기에 if문 필요없음.
            cur = cur.child[w]  # 자식노드
            s += cur.string  # 현재까지 탐색한 부분
            # count 1이면 유일한 단어이니 반환. 단어가 일치해도 반환.
            if cur.count == 1 or s == word:
                return idx

def solution(words):
    # words에 있는 단어들은 모두 학습됨.
    # 각 단어들을 다시 검색할 때 몇 글자를 입력해야 자동완성되는가를 전부 더해서 리턴
    # 단어 수 N: 2~10만,  단어 길이 총 합 L: 2~100만
    root = Trie()
    for word in words:
        root.insert(word)
    ans = 0
    for word in words:
        ans += root.search(word)  # 찾는데 필요한 최소 글자 수 더해주기
    return ans

inputdatas = [
    ['go', 'gone', 'guild'],
    ['abc', 'def', 'ghi', 'jklm'],
    ['word', 'war', 'warrior', 'world'],
    ['a' * 999998, 'bc']
]

"""
2018 카카오 공채 기출. Lv.4. 
보자마자 생각난 방법이 여럿이었다.
딕셔너리에 자식기록, 스트링의 startswith 사용, 노드 사용.
다른건 시간초과가 발생할 것 같아서 글자별로 노드 만들어서 자식 이어주는 것부터 해보자고 생각했다.
그렇게 노드를 만드는건 쉬웠는데, 단어를 찾는 과정에서 
최소 글자 수를 리턴하는걸 구현하는 과정에서 헷갈려서 꼬였다.
1시간 43분쯤에 겨우 예시케이스를 통과하도록 작성이 완료되었고, 테케 9, 10에서 런타임 에러가 발생했다.
처음엔 재귀 깊이 문제인 줄 알았으나, sys.setrecursionlimit으로 깊이를 늘려줘도 그대로였다.
존재할 수 있는 가장 긴 단어인 99만 9998자의 단어를 테케에 넣어봐도 통과했다.
시간초과의 경우 '런타임 에러'가 발생하지 않는다.
원인은 찾지 못했고, 내가 작성한 노드 사용법이 '트라이'라는 자료구조였다.
그런데 이전에 내가 짰던 트라이 구조에 비해 엉망이었다. 트라이 구조를 다시 짜봤더니 그냥 통과했다.
트라이 구조에 익숙했다면 30분 내에 풀지 않았을까 싶다.
다 지우고 트라이로 다시 풀어봤더니 구현에 5분 30초 걸렸다. 
데이터 옮겨적고 문제 이해하고 트라이 구조 기억해내고 
문제에 맞게 변형할 아이디어 얻는 시간을 생각해보면 30분이면 풀 것 같다.
결국 트라이 자료구조 연습부족이 불러온 실태.
"""

for t in inputdatas:
    print(solution(t))
