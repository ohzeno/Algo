# https://www.acmicpc.net/problem/2224
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tmp = {}
count = 0
for _ in range(n):
    a, pointer, b = input().split()
    if a != b:
        if a in tmp:  # 이미 키가 있으면
            if b not in tmp[a]:  # 같은 명제 여러 번 주어질 수 있음
                tmp[a].append(b)
                count += 1
        else:  # 키 없으면 생성
            tmp[a] = deque([b])
            count += 1
for key, value in tmp.items():
    tmp_value = deepcopy(value)  # append할 예정이기에 원본이 아닌 복사본 사용
    while tmp_value:   # key가 전건인 명제가 있으면
        val = tmp_value.popleft()  # 후건 받아와서
        if val in tmp:  # 해당 문자를 전건으로 사용하는 명제가 있으면
            for va in tmp[val]:  # 해당 문자에서 이어지는 후건들 받아와서
                # 최초 전건이랑 마지막 후건이 같지 않고
                if key != va and va not in tmp[key]:  # 혹시나 탐색중에 중복 생길까봐
                    tmp[key].append(va)  # 명제목록에 추가
                    tmp_value.append(va)  # 후건을 거쳐가는 명제 확인
                    count += 1
print(count)
for key in sorted(list(tmp)):  # 딕셔너리 키는 정렬되어있지 않다.
    for val in sorted(tmp[key]):  # 후건 정렬
        print(f'{key} => {val}')


