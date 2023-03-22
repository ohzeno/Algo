# https://www.acmicpc.net/problem/15652
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n, m이 주어짐. 다음을 만족하는 길이 m인 수열을 모두 구하라.
1부터 n까지 자연수 중에서 m개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
    길이가 k인 수열 A가 A1 ≤ A2 ≤ ... ≤ Ak-1 ≤ Ak를 만족하면 비내림차순이라고 한다.
"""
n, m = map(int, input().split())
arr = []

def dfs(st):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(st, n+1):  # 사전순
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)

"""
현 시점 실버3. 제출 41038, 정답률 78.789%
"""