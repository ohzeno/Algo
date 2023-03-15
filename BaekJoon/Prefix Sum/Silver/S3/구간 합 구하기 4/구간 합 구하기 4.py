# https://www.acmicpc.net/problem/11659
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
리스트와 구간이 주어지면 구간합을 구하라.
"""
n, m = map(int, input().split())
datas = list(map(int, input().split()))
for i in range(1, n):
    datas[i] += datas[i-1]
for _ in range(m):
    i, j = map(int, input().split())
    print(datas[j-1] - datas[i-2] if i > 1 else datas[j-1])


"""
현 시점 실버3. 제출 67551, 정답률 40.306%
m이 10만까지 커지기에 매번 sum을 쓸 수는 없다. 누적합 문제
"""