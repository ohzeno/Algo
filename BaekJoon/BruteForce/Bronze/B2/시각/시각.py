# https://www.acmicpc.net/problem/18312
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n, k가 입력되면 00시 00분 00초부터 n시 59분 59초까지 모든 시각 중에서 
k가 하나라도 포함되는 모든 시각을 세는 프로그램을 작성하라.
"""

n, k = map(int, input().split())
ans = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(k) in str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2):
                ans += 1
print(ans)
