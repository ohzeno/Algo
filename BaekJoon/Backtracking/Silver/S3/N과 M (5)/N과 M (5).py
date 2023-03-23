# https://www.acmicpc.net/problem/15654
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n, m이 주어짐. 다음을 만족하는 길이 m인 수열을 모두 구하라.
n개의 자연수 중에서 m개를 고른 수열
"""
n, m = map(int, input().split())
datas = sorted(map(int, input().split()))
arr = []

def dfs():
    if len(arr) == m:
        print(*list(arr))
        return
    for i in range(n):  # 사전순
        if datas[i] in arr:
            continue
        arr.append(datas[i])
        dfs()
        arr.pop()

dfs()

# from itertools import permutations
# cases = list(permutations(datas, m))
# for case in cases:
#     print(*case)

"""
현 시점 실버3. 제출 25671, 정답률 72.662%
permutations를 쓰고싶어지는 문제. 조건을 보면 애매하지만 예제를 보면 순열이다.
"""