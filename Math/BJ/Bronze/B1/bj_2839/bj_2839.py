# https://www.acmicpc.net/problem/2839
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
count_5 = n // 5  # 5kg봉지 최대값
end = 0
while count_5 >= 0:
    if (n - 5 * count_5) % 3 == 0:  # 5kg 현재 갯수 쓰면 나누어 떨어질 때
        print(count_5 + (n - 5 * count_5) // 3)
        end = 1
        break
    else:
        count_5 -= 1  # 안되면 5kg 갯수 줄여봄
if count_5 < 0:
    count_5 = 0
if not end:  # end가 1이 아니면 3, 5킬로로 나누어 떨어지지 않음.
    print(-1)
