# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
class LRUCache_dict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
    def get(self, key: int) -> int:
        if key in self.cache:  # 이미 존재하면
            val = self.cache.pop(key)  # 제거
            self.cache[key] = val  # 재할당으로 최근 사용으로 간주
            return val
        return -1  # 없으면 -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # 이미 존재하면
            self.cache.pop(key)  # 제거
        elif self.size == self.capacity:  # 캐시가 꽉 차있으면
            self.cache.pop(next(iter(self.cache)))  # 가장 오래된(앞쪽) 키 제거
        else:  # 존재하지 않고, 캐시가 꽉 차있지 않으면 사이즈 업
            self.size += 1
        self.cache[key] = value  # 재할당/신규 할당

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.nxt = None
        self.prv = None

class LRUCache_linkedlist:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 링크드 리스트 탐색은 오래걸리므로 따로 딕셔너리 사용.
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # 따로 안빼두면 delete때문에 add할 때 val을 특정할 수 없다.
            # add 먼저 하고 delete하면 cache에서 key가 사라져서 val을 리턴하지 못한다.
            val = self.cache[key].val
            self.delete(key)
            self.addToTail(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)  # 키가 있다면 뒤로 빼주기 위해 삭제
        elif self.size == self.capacity:  # 용량 초과
            self.delete(self.head.key)  # 가장 오래된(앞쪽) 키 제거
        self.addToTail(key, value)  # 신규/재할당

    def addToTail(self, key, val):
        node = Node(key, val)
        if not self.head:  # 아직 헤드가 없으면 헤드로 지정
            self.head = node
        elif not self.tail:  # 헤드는 있지만 테일이 없으면 테일로 지정
            self.tail = node
            self.head.nxt = self.tail
            self.tail.prv = self.head
        else:  # 헤드와 테일이 모두 있으면 테일에 연결
            self.tail.nxt = node
            node.prv = self.tail
            self.tail = node
        self.cache[key] = node  # 캐시에 추가
        self.size += 1

    def delete(self, key):
        node = self.cache.pop(key)  # 캐시에서 제거
        if node.prv:  # 노드가 헤드가 아니면
            node.prv.nxt = node.nxt  # 앞쪽이랑 뒤쪽 연결
        else:  # 노드가 헤드면 뒤쪽을 헤드로
            self.head = node.nxt
        if node.nxt:  # 노드가 테일이 아니면
            node.nxt.prv = node.prv  # 앞쪽이랑 뒤쪽 연결
        else:  # 노드가 테일이면 앞쪽을 테일로
            self.tail = node.prv
        self.size -= 1

inputdatas = [
    [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]],
    [["LRUCache","put","put","get","get","put","get","get","get"],
    [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]]
]
lru = LRUCache_linkedlist(inputdatas[0][1][0][0])
for i in range(len(inputdatas)):
    for order, data in zip(inputdatas[i][0], inputdatas[i][1]):
        if order == "put":
            lru.put(data[0], data[1])
        elif order == "get":
            print(lru.get(data[0]))
    print()
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
LeetCode Medium. 처음에 LRU 해석을 잘못 해서 가장 최근에 사용된 키를 제거 하라는 줄 알았다.
딕셔너리와 next, iter를 사용해 풀었는데 사람들 반응을 보니 
인터뷰어가 dict가 ordered되어있는 걸 이용 하지 말라고 할 거라고 한다.

그에 대비해 링크드 리스트를 이용한 풀이도 작성해 봤으나 작성에 시간이 오래 걸렸다.
케이스를 하나 하나 고려하는 빡구현 문제 느낌이다.
"""

