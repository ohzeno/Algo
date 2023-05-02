# https://www.acmicpc.net/problem/1991
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def pre_order(cur):
    ans = chr(cur + default)
    if lcs[cur] != -1:
        ans += pre_order(lcs[cur])
    if rcs[cur] != -1:
        ans += pre_order(rcs[cur])
    return ans

def post_order(cur):
    ans = ''
    if lcs[cur] != -1:
        ans += post_order(lcs[cur])
    if rcs[cur] != -1:
        ans += post_order(rcs[cur])
    ans += chr(cur + default)
    return ans

def in_order(cur):
    ans = ''
    if lcs[cur] != -1:
        ans += in_order(lcs[cur])
    ans += chr(cur + default)
    if rcs[cur] != -1:
        ans += in_order(rcs[cur])
    return ans

# 트리 입력되면 전위/중위/후위 순회 결과를 한 줄씩 리턴
# N은 1~26
n = int(input())
lcs = [-1] * n
rcs = [-1] * n
default = ord('A')
for _ in range(n):
    p, lc, rc = input().split()
    p, lc, rc = map(lambda x: ord(x) - default, [p, lc, rc])
    if lc > 0:
        lcs[p] = lc
    if rc > 0:
        rcs[p] = rc

print(pre_order(0))
print(in_order(0))
print(post_order(0))

"""
트리문제. 풀이 당시 난이도 S1. 정답률 69.966%
옮겨적기, 제출까지 14분 걸렸다.
전위/중위/후위 순회 문제. 풀이 당시 중위순회 영어로 뭐였는지 생각 안났었다...
나는 리스트를 사용하기 위해 알파벳을 숫자로 변형했는데
다른 풀이를 보니 딕셔너리를 사용해서 편하게 풀이했다. 그렇게 풀었으면 시간 단축 가능할듯.
"""
