# https://www.acmicpc.net/problem/2133
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
"""

def tiling(n):
    if n % 2:
        return 0
    dp = [0] * (n+1)
    dp[0], dp[2] = 1, 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 4 - dp[i-4]
    return dp[n]

print(tiling(int(input())))

"""
현 시점 골드 4. 제출 46718. 정답률 35.873%
dp[6]까진 구하면 억지 논리로라도 점화식을 만드는데 직접 구하기 힘들다.
한국 블로거들은 죄다 dp[6]까지만 자신의 논리로 설명하고 
dp[8] 식에 대해서는 자신의 논리와 맞지 않음에도 설명을 생략한다.
그 상태로 논리를 비약하여 점화식을 만들어낸다.
외국의 경우, 오른쪽 끝의 한 칸이 비어있는 경우를 이용하여
f, g 두 식을 만들어 점화식을 만들어내기도 하지만 역시 점화식 도출 과정을 생략하는 경우가 많다.
점화식 도출 과정에 대한 질문이 생기면 '설명에 다 나와있다'는 억지만 부리고 
도출 과정을 설명하는 사람은 없다.

원본은 Waterloo local 2005.09.24 문제이며, 
블로그 퍼와서 푸는 사람들만 없었더라도 골드4는 아니었을 것이다.
FRT(도형 추리 검사) 상위 1% 이내이고 물리학과인 내가 점화식 도출에 몇 시간이 걸렸다.
처음 풀면서 블로그 풀이 보지 않고 점화식을 30분 안에 도출할 수 있는 사람은
ICPC 선수급이 아니라면 0.1%도 없을거라 확신한다.
프로그래머스는 처음엔 Lv.4로 분류했으나, 추후 Lv.2로 강등됐다.
개인적으로 Lv.4가 맞다고 생각한다.

홀수 i에 대해서는 2x1 블럭이 2칸이므로 홀수칸을 채울 수 없어 0이다.
짝수 칸에 대해서 점화식을 만들어야 한다.
dp[i]는 dp[i-2]에 2칸을 더했다고 생각할 수 있다.
오른쪽 2칸을 채우는 중복되지 않는 방법은 dp[2]이며
왼쪽은 dp[i-2]다.
짝수 i마다 양 모서리에 세로블럭을 두고 
가운데를 가로 블럭으로 채우는(0개 채우면 dp[2]) 
독립 패턴이 2개(첫줄, 막줄 가로 막대로 채움) 있다.

dp[2]
자체적으로 2칸 독립패턴이므로
    dp[2] = 3(오른쪽 2칸) * dp[0](왼쪽0칸)
    
dp[4]
오른쪽 2칸 독립패턴에 대해 왼쪽 2칸 경우의 수를 곱하고
4의 독립 패턴을 더해준다.
    dp[4] = 3 * dp[2] + 2
    
dp[6]
오른쪽 2칸 독립 패턴에 대해 왼쪽 4칸 경우의 수를 곱하고
오른쪽 4칸 독립 패턴에 대해 왼쪽 2칸 경우의 수를 곱하고
(독립패턴만 곱하는 이유는 4+2에 오른쪽 4의 독립 패턴을 제외한 2+4패턴이 이미 포함되기 때문이다.)
6의 독립 패턴을 더해준다.
    dp[6] = 3 * dp[4] + 2 * dp[2] + 2
dp[8]
오른쪽 2칸 독립 패턴에 대해 왼쪽 6칸 경우의 수를 곱하고
오른쪽 4칸 독립 패턴에 대해 왼쪽 4칸 경우의 수를 곱하고
오른쪽 6칸 독립 패턴에 대해 왼쪽 2칸 경우의 수를 곱하고
8의 독립 패턴을 더해준다.
    dp[8] = 3 * dp[6] + 2 * dp[4] + 2 * dp[2] + 2
    
즉 dp[i] = 3 * dp[i-2] + 2 * dp[i-4] + 2 * dp[i-6] + ... + 2
dp[i-2] = 3 * dp[i-4] + 2 * dp[i-6] + 2 * dp[i-8] + ... + 2

위 두 식을 연립하여 정리하면
dp[i] = 4 * dp[i-2] - dp[i-4]
"""