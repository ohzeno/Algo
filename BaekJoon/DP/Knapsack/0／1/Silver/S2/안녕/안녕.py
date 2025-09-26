# https://www.acmicpc.net/problem/1535
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
사람의 번호는 1번부터 N(<=20)번까지 있다. 
세준이가 i번 사람에게 인사를 하면 
    L[i]만큼의 체력을 잃고, 
    J[i]만큼의 기쁨을 얻는다. 
세준이는 각각의 사람에게 최대 1번만 말할 수 있다.
세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다. 
초기 체력은 100이고, 기쁨은 0이다. 
만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다. 
얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성하시오.
"""

N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
# dp[i] = 체력 i를 사용했을 때 얻을 수 있는 최대 기쁨
dp = [0] * 100  # 체력을 0~99까지 사용 가능

# i번 사람에게 인사를 하는 경우
for i in range(1, N + 1):
    # 앞쪽을 참조하므로 중복 인사 방지를 위해 뒤에서부터 업데이트 (0/1 배낭)
    for j in range(99, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(max(dp))


"""
현 시점 Silver II. 제출 14771. 정답률 57.296 %
무한배낭 G4에서 막히고 나서 배낭공부를 위해 풀었는데 0/1배낭이 나왔다.
배낭 문제 자체 경험이 3문제 뿐이라 아직 익숙치 않은듯. 실버도 dp 정의에 애를 먹었다.
"""
