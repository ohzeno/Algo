# https://school.programmers.co.kr/learn/courses/30/lessons/60060
class Node:
    def __init__(self, key):
        self.key = key  # 디버깅때 무슨 글자인지 보는 용도
        self.child = {}  # 자식 기록
        self.wl_count = {}  # 현 글자까지 포함하는 단어들의 길이별로 갯수 기록

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        len_word = len(word)
        if len_word in cur.wl_count:  # 글자수별 기록
            cur.wl_count[len_word] += 1
        else:
            cur.wl_count[len_word] = 1
        for w in word:
            cur = cur.child.setdefault(w, Node(w))  # 자식노드 생성해서/이미 있으면 노드반환
            if len_word in cur.wl_count:  # 글자수별 기록
                cur.wl_count[len_word] += 1
            else:
                cur.wl_count[len_word] = 1

    def search(self, word):
        cur = self.head
        len_word = len(word)
        if word == '?' * len_word:  # 전부 ?이면 head에 기록있나 보고 반환
            if len_word in cur.wl_count:
                return cur.wl_count[len_word]
            else:
                return 0
        for w in word:
            if not cur.child:  # 단어인데 자식 없으면 0 반환
                return 0
            if w != '?':  # ?가 아니면 자식노드로
                if w in cur.child:
                    cur = cur.child[w]
                else:  # 해당 글자에 해당하는 자식 없으면 0 반환
                    return 0
            else:  # 처음 ?나오면 길이별 카운트 반환.
                if len_word in cur.wl_count:
                    return cur.wl_count[len_word]
                else:
                    return 0

def solution(words, queries):
    # words에는 가사에 사용된 모든 단어가 있음.
    # queries는 찾고자 하는 키워드가 담긴 배열
    # 각 키워드별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환.
    # words는 2~10만    각 단어 길이는 1~1만
    # 전체 가사 단어 길이 합은 2~100만
    # words에 중복단어 없음.
    # 전부 알파벳 소문자.
    # queries는 2~10만    각 키워드 1~1만
    # 전체 검색 키워드 길이 합 2~100만
    # 검색 키워드는 중복 있을 수 있음.
    # 알파벳 소문자, ?로만 구성.
    # ?는 접두사 아니면 접미사로만 주어짐.
    ans = []
    foward = Trie()  # 정방향 트라이
    backward = Trie()  # 역방향 트라이
    already_found = {}  # 이미 탐색한 케이스

    def logging(word):
        if word in already_found:  # 탐색기록 있으면 그대로 기록
            ans.append(already_found[word])
        else:  # 탐색기록 없으면
            if word[0] == '?':  # '?'로 시작하면 거꾸로 바꿔서 backword 탐색.
                word = word[::-1]
                data = backward.search(word)
            else:  # 아니면 foward 탐색
                data = foward.search(word)
            ans.append(data)  # 정답에 갯수 기록하고
            already_found.setdefault(word, data)  # 탐색기록

    for word in words:  # 트라이 생성
        foward.insert(word)
        backward.insert(word[::-1])
    for query in queries:  # 쿼리별 결과 기록
        logging(query)
    return ans

inputdatas = [
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "fro???", "pro?"]],
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]],
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["???????"]],
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "fro??", "fro??", "fro??", "fro??"]],
]

"""
2020 카카오 공채 기출. Lv.4.
46분에 초안 제출. 효율성테스트 1, 3에서 시간초과 발생.
단어 총 글자수를 노드마다 기록해두고, 글자수 자식이 존재하지 않으면 리턴,
자식 탐색 중에 글자수 자식이 존재하지 않으면 넘어가도록 작성.
49분에 해당 코드 제출, 여전히 효율성 1, 3케이스 시간초과.
쿼리가 '?'로만 이루어진 경우 탐색하지 않도록, 글자수마다 단어 갯수를 기록해놓고 반환하도록 함.
51분에 해당 코드 제출, 효율성 1 시간초과.
쿼리에 중복만 가득한 경우 대비해 이미 찾은 케이스 기록해서 리턴하도록 수정.
53분에 해당 코드 제출, 효율성 1 시간초과.
자식들 재귀탐색 하는 과정 메모이제이션 적용.
60분에 해당 코드 제출, 효율성 1, 4, 5 시간초과.

삽입 시에 각 노드에 단어 길이별 카운트를 만들어놓고 ?에 도달하면 글자수에 맞는 카운트를 반환하도록 교체.
이전에 기록하던건 트라이 밖에서 단어 길이병 총 갯수만 적어놨었다. 이번엔 노드마다 현 노드에서 이어지는 단어 길이별 카운트를 기록해서 '?'를 전부 탐색하지 않도록 했다.
120분에 해당 코드 제출, 통과.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
