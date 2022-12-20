# https://www.acmicpc.net/problem/2224
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tmp = [[] for _ in range(58)]
count = 0
"""
딕셔너리와 같은 로직. ord만 사용함. 
heapq 사용하면 sort 사용 안해도 될듯.
"""
for _ in range(n):
    a, pointer, b = input().split()
    if a != b and ord(b) - 65 not in tmp[ord(a) - 65]:
        tmp[ord(a) - 65].append(ord(b) - 65)
        count += 1
for i in range(58):
    tmp_value = tmp[i][:]
    while tmp_value:
        val = tmp_value.pop()
        if tmp[val]:
            for va in tmp[val]:
                if i != va and va not in tmp[i]:
                    tmp[i].append(va)
                    tmp_value.append(va)
                    count += 1
print(count)
for i in range(58):
    if tmp[i]:
        for val in sorted(tmp[i]):
            print(f'{chr(i + 65)} => {chr(val + 65)}')



