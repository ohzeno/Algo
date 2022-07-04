# https://www.acmicpc.net/problem/1978
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = list(map(int, input().split()))
ans = 0
for data in datas:
    if data == 1:  # 1은 소수 아님. 다음 숫자.
        continue
    for i in range(2, data):  # 1과 자신 제외한 수
        if data % i == 0:  # 나누어 떨어지면 소수 아님
            break
    else:  # break 안됐으면 소수
        ans += 1
print(ans)
