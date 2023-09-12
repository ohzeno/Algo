# https://school.programmers.co.kr/learn/courses/30/lessons/12980
"""
"""
def solution(n):
    ans = 0
    while n:
        ans += n % 2
        n //= 2
    return ans
    # dp = [0] * (n+1)
    # for i in range(1, n+1):
    #     if i % 2:
    #         dp[i] = dp[i-1] + 1
    #     else:
    #         dp[i] = dp[i//2]
    # return dp[n]
    # return bin(n).count('1')

inputdatas = [
    4, 5, 6, 8, 5000
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.2. 현 시점 완료한 사람 15,113명, 정답률 68%

효율성 때문에 레벨 4로 느껴졌다.
정답률 68%인 이유는 그냥 블로그 풀이가 널려서 그런듯.
코테에서 만나면 이걸 풀 사람은 몇 없을 것이다.

시뮬레이션이 먼저 생각났는데,
그냥 역순으로 일반화하했다.
홀수 칸이면 끝에서 한 칸 점프가 필요하다.
배터리 사용량을 최저로 하려면 점프를 짧게 해야하는데,
순간이동은 2배수로만 움직일 수 있기 때문에 짝수칸까지 가게된다.
처음부터 2칸 움직인 후 배수로 움직여도 소모량은 똑같다.
짝수칸의 경우 2로 나누다보면 결국 1이 되어 점프로 끝낼 수 있다.

위 풀이는 dp였는데 효율성을 통과하지 못했다.
해당 과정을 while문으로 바꿔주면 n을 전부 순회하지 않아서 통과된다.

2진수로 바꾸고 1의 개수를 세는 방법도 있던데 직관적이진 않다.
"""

for t in inputdatas:
    print(solution(t))
