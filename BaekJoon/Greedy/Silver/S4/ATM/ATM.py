# https://www.acmicpc.net/problem/11399
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# 각 사람이 돈을 인출하는 데 필요한 최소 시간이 주어짐.
# 순서를 바꿔서 각 사람이 돈을 인출하기 위한 시간의 총 합 최소?
# 첫 사람이 3분, 두 번째 사람이 4분 걸린다면 두 번째 사람은 첫 사람 시간까지 7분 걸린다.
n = int(input())
datas = sorted(list(map(int, input().split())))  # 누적 시간이기에 앞쪽이 최소가 되어야 한다.
ans = acc = 0
for d in datas:
    acc += d  # 지금 사람 인출에 걸린 총 시간.
    ans += acc
print(ans)


# 현 난이도 S4. 정답률 67.545%. 문제 읽고 제출까지 9분 걸렸다.
