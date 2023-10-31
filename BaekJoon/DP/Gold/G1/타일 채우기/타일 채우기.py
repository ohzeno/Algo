# https://www.acmicpc.net/problem/2718
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
4xn 타일을 1x2, 2x1 블럭으로 채우는 방법의 수를 반환하라.
"""
# def sol(n):
    # dp = [0] * (n+1)
    # dp[0] = 1
    # for i in range(1, n+1):  # i가 1일 경우 dp[-1]은 아직 0이므로 그대로 사용 가능
    #     dp[i] = dp[i-1] + dp[i-2] * 4
    #     sc = 2
    #     for j in range(i-3, i-3-(n-2), -1):
    #         dp[i] += dp[j] * sc
    #         sc = 3 if sc == 2 else 2
    # dp[0:4] = [1, 1, 5, 11]
    # for i in range(4, n+1):
    #     dp[i] = dp[i-1] + dp[i-2] * 5 + dp[i-3] - dp[i-4]
    # return dp[n]
    # a, b, c, d = 1, 1, 5, 11
    # for _ in range(n-1):
    #     d, a, b, c = d + c*5 + b - a, b, c, d
    # return b

for _ in range(int(input())):
    # print(sol(int(input())))
    a, b, c, d = 1, 1, 5, 11
    for _ in range(int(input())-1):
        d, a, b, c = d + c*5 + b - a, b, c, d
    print(b)

"""
현 시점 골드 1. 제출 2439. 정답률 65.521%
dp[1]
    0 * dp[1]
    1독립 패턴 1개
    dp[1] = 1(세로 두개)
dp[2]
    dp[1] * dp[1]
    2독립 패턴 4개
    dp[2] = dp[1] + 4(가로4/ 가로2, 세로2 3패턴) = 5
dp[3]
    dp[2] * dp[1]
    dp[1] * 2독립패턴 4개
    3독립 패턴(위쪽 2칸 |=, 아래 2칸 =|, 반대) 2개
    dp[3] = dp[2] + dp[1] * 4 + 2 = 11
dp[4]
    dp[3] * dp[1]
    dp[2] * 2독립패턴 4개
    dp[1] * 3독립패턴 2개
    4독립 패턴(--, |=|, -- 3패턴) 3개
    dp[4] = dp[3] + dp[2] * 4 + dp[1] * 2 + 3 = 36
dp[5]
    dp[4] * dp[1]
    dp[3] * 2독립패턴 4개
    dp[2] * 3독립패턴 2개
    dp[1] * 4독립패턴 3개
    5독립 패턴(==|, |==, 반대) 2개
    dp[5] = dp[4] + dp[3] * 4 + dp[2] * 2 + dp[1] * 3 + 2 = 95
dp[6]
    dp[5] * dp[1]
    dp[4] * 2독립패턴 4개
    dp[3] * 3독립패턴 2개
    dp[2] * 4독립패턴 3개
    dp[1] * 5독립패턴 2개
    6독립 패턴(---, |==|, --- 3패턴) 3개
    dp[6] = dp[5] + dp[4] * 4 + dp[3] * 2 + dp[2] * 3 + dp[1] * 2 + 3 = 281
dp[7]
    dp[6] * dp[1]
    dp[5] * 2독립패턴 4개
    dp[4] * 3독립패턴 2개
    dp[3] * 4독립패턴 3개
    dp[2] * 5독립패턴 2개
    dp[1] * 6독립패턴 3개
    7독립 패턴(===|, |===, 반대) 2개
    dp[7] = dp[6] + dp[5] * 4 + dp[4] * 2 + dp[3] * 3 + dp[2] * 2 + dp[1] * 3 + 2 = 781
즉, 
dp[n] = dp[n-1] + dp[n-2] * 4 + 0까지 한 인덱스씩 내려가며 2, 3을 번갈아 곱하고 더해줌.(n>=2)
홀, 짝에 따라 점화식이 다른데
어느쪽이든 dp[n-2] 식과 연립하면
dp[n] = dp[n-1] + dp[n-2] * 5 + dp[n-3] - dp[n-4](n>=4)가 나온다.
"""