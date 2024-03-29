# https://www.acmicpc.net/problem/1463
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  # 1을 빼는 경우
    if i % 2 == 0:  # 2로 나누는 경우
        dp[i] = min(dp[i], dp[i//2] + 1)  # 2로 나누는 경우와 1을 빼는 경우 중 작은 값
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])

"""
현 시점 실버3. 제출 247308, 정답률 32.440%
처음엔 bfs로 각 수의 dp테이블을 만들어보고 일반항 규칙을 찾을까 했다.
10까지 dp테이블을 만들어봐도 규칙성이 보이지 않아서 그렇게 생각했었는데
케이스를 나눠서 생각하면 규칙을 찾을 수 있었다.
dp에 익숙치 않아서 그런지 골드 풀 때보다 어려웠다.
"""