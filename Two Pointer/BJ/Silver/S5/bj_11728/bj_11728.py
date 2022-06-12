# https://www.acmicpc.net/problem/11728
import sys
sys.stdin = open('input.txt')

def input():
    return sys.stdin.readline().rstrip()
la, lb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 단순 리스트 합치기, 정렬
# c = a + b
# c.sort()
# print(*c)

# 투 포인터
ia, ib = 0, 0
res = []
# 둘 비교하면서 작은거 추가
while ia < la and ib < lb:
    if a[ia] < b[ib]:
        res.append(a[ia])
        ia += 1
    else:
        res.append(b[ib])
        ib += 1
# 남은 리스트 원소들 쭉 추가. 각 리스트들이 정렬되어 있기에 가능함.
while ia < la:
    res.append(a[ia])
    ia += 1
while ib < lb:
    res.append(b[ib])
    ib += 1

print(*res)
