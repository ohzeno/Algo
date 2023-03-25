# https://www.acmicpc.net/problem/15663
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n, m이 주어짐. 다음을 만족하는 길이 m인 수열을 모두 구하라.
n개의 자연수 중에서 m개를 고른 수열
"""
n, m = map(int, input().split())
datas = list(map(int, input().split()))
idxs = set()  # visited 써도 된다.
arr = []
ans = set()
def dfs():
    if len(arr) == m:
        ans.add(tuple(arr))  # 중복 제거
        return
    for i in range(n):
        if i in idxs:
            continue
        idxs.add(i)
        arr.append(datas[i])
        dfs()
        arr.pop()
        idxs.remove(i)

dfs()
for case in sorted(ans):
    print(*case)

# from itertools import permutations
# cases = list(set(permutations(datas, m)))
# for case in sorted(cases):
#     print(*case)

"""
현 시점 실버2. 제출 27810, 정답률 49.134%
같은 원소가 들어가면 안되지만 값이 중복인 원소가 있길래 
당황해서 idxs를 set에 기록해서 풀었는데
나중에 생각해보니 dfs니까 visited 사용하면 되는거였다...
물론 permutations를 쓰면 더 쉽다.
"""