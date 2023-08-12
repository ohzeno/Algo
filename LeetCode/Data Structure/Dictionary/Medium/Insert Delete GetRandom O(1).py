# https://leetcode.com/problems/insert-delete-getrandom-o1/
from typing import Optional, List
"""
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
import random
class RandomizedSet:
    def __init__(self):
        self.idx_d = {}
        self.arr = []
        self.idx = 0  # 기록용 인덱스

    def insert(self, val: int) -> bool:  # 없으면 삽입하고 True. 있으면 False
        if val not in self.idx_d:
            self.arr.append(val)
            self.idx_d[val] = self.idx
            self.idx += 1
            return True
        return False

    def remove(self, val: int) -> bool:  # 있으면 제거하고 True. 없으면 False
        if val in self.idx_d:
            self.arr[self.idx_d[val]] = self.arr[-1]  # 마지막 원소를 제거할 원소의 위치로 옮겨줌
            self.idx_d[self.arr[-1]] = self.idx_d[val]  # 마지막 원소의 인덱스를 제거할 원소의 인덱스로 바꿔줌
            self.arr.pop()  # 제거할 원소는 이미 마지막 원소로 덮어씌워짐. 마지막 원소는 중복이니 제거.
            self.idx_d.pop(val)  # 제거한 원소의 인덱스 기록 제거.
            self.idx -= 1
            return True
        return False

    def getRandom(self) -> int:  # 랜덤하게 하나 반환. set에서 제거하지 않음. 원소 있을 때만 호출됨.
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

inputdatas = [
    [["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
     [[], [1], [2], [2], [], [1], [2], []]]
]

"""
LeetCode Medium
12분쯤 걸려서 set와 random을 사용해 있는 그대로 구현했다.
insert, remove, getRandom을 O(1)으로 구현하라고 했는데, 
기존 내 풀이는 getRandom에서 set를 list로 변환해야 해서 시간이 오래걸렸다.
Editorial에서 dict와 list를 사용해 O(1)을 구현하는 방법을 배워 다시 풀었다.
원소를 추가하면 dict에 val: idx로 기록하고,
제거할 때는 dict에서 idx를 가져와서 리스트 마지막 원소를 제거할 원소의 위치에 넣고, 인덱스를 업데이트 한다.
그 후 pop으로 끝 원소를 제거하고 dict에서도 제거한다.
그러면 getRandom에서 set를 list로 바꿀 필요 없이 저장된 list에서 랜덤하게 하나를 뽑으면 된다.
"""
obj = RandomizedSet()
for order, num in zip(inputdatas[0][0][1:], inputdatas[0][1][1:]):
    if order == "insert":
        print(obj.insert(num[0]))
    elif order == "remove":
        print(obj.remove(num[0]))
    elif order == "getRandom":
        print(obj.getRandom())

