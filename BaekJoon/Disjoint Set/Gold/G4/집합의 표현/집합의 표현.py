# https://www.acmicpc.net/problem/1717
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, n_oper = map(int, input().split())
"""
dict, set 이용해봤는데 메모리 초과.
"""
# set_ = {}
# for i in range(n + 1):
#     set_[i] = {i}
# for _ in range(n_oper):
#     oper, a, b = map(int, input().split())
#     if oper == 0:
#         set_[min(a, b)].union(set_[max(a, b)])
#     elif oper == 1:
#         if max(a, b) in set_[min(a, b)]:
#             print('YES')
#         else:
#             print('NO')
p = [i for i in range(n + 1)]
def find_set(x):
    fn = x
    while p[x] != x:
        x = p[x]
    p[fn] = x  # 최초 원소 부모 갱신. 경로단축. 이거 안하면 시간초과.
    return x

def union(x, y):
    if x == y:
        return
    nx = find_set(x)
    ny = find_set(y)
    p[max(nx, ny)] = min(nx, ny)

for _ in range(n_oper):
    oper, a, b = map(int, input().split())
    if oper == 0:  # 병합명령
        union(a, b)
    elif oper == 1:  # 확인명령
        if find_set(a) == find_set(b):  # 동일 집합에 있으면 yes
            print("YES")
        else:
            print("NO")
