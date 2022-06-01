# https://www.acmicpc.net/problem/14916
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())

count_5 = n // 5  # 5원 동전 최대 갯수
end = 0
while count_5 >= 0:  # 5원동전 갯수 마이너스면 중단
    if (n - count_5 * 5) % 2 == 0:  # 현재 5원 갯수만큼 빼고 남은 돈이 2원으로 나누어 떨어지면 브레이크
        end = 1
        break
    else:  # 나누어 떨어지지 않으면 5원 동전 갯수 줄여봄.
        count_5 -= 1
if count_5 < 0:  # 5원 갯수 음수 됐으면 0으로
    count_5 = 0
if end:  # 2, 5원으로 나누어 떨어졋으면 5원 갯수, (5원 빼고 남은 돈//2) 2원 갯수
    print(count_5 + (n - count_5 * 5) // 2)
else:  # while 끝나고도 end가 아니면 나누어 떨어지지 않으니 -1 출력
    print(-1)


