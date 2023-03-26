# https://www.acmicpc.net/problem/15666
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n, m이 주어짐. 다음을 만족하는 길이 m인 수열을 모두 구하라.
n개의 자연수 중에서 m개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
    길이가 k인 수열 A가 A1 ≤ A2 ≤ ... ≤ Ak-1 ≤ Ak를 만족하면 비내림차순이라고 한다.
"""
n, m = map(int, input().split())
datas = sorted(map(int, input().split()))
arr = []
check = set()

def dfs(st):
    if len(arr) == m:
        tmp = tuple(arr)
        if tmp not in check:  # 중복 제거
            print(*tmp)
        check.add(tmp)
        return
    for i in range(st, n):  # 사전순
        arr.append(datas[i])
        dfs(i)
        arr.pop()

dfs(0)


"""
현 시점 실버2. 제출 13077, 정답률 80.732%
"""