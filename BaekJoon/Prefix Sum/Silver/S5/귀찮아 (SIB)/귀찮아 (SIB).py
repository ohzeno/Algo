# https://www.acmicpc.net/problem/14929
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = list(map(int, input().split()))
ans = 0
presum = [sum(datas) - datas[0]]
for i in range(1, n - 1):
    presum.append(presum[i - 1] - datas[i])
for j in range(n - 1):
    ans += datas[j] * presum[j]
print(ans)
"""
2중 for문으로 다 더하면 n^2 만큼의 +와 *연산이 필요하다.
각 원소끼리 곱하는 표를 만들어보면 대각선 위쪽 삼각형의 합이 된다.
그 삼각형 내의 각 행은 i행 원소 * (i행 이후 모든 원소의 합)이다.
presum[i]는 datas[i]에 곱해줘야 할 부분합이다.
이렇게 하면 n만큼의 -연산, append연산, 2n만큼의 +(sum 포함), *연산이 필요하다.
계수가 상수이므로 n이 커질수록 n^2에 비해 소모시간이 짧아진다.
"""