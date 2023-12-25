# https://www.acmicpc.net/problem/1107
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
리모컨에는 0~9, +, - 버튼이 있다.
채널 0에서 -를 눌러도 채널은 변하지 않는다.
채널은 무한대 만큼 있다.
고장난 버튼이 주어진다.
100번에서 N채널로 이동하기 위해 최소 몇 번 버튼을 눌러야 하는가?
0 <= N <= 50_0000
"""
def solution():
    n = int(input())
    if n == 100:
        return 0
    res = abs(n-100)  # 100에서 +, - 버튼만으로 이동하는 경우
    m = int(input())
    if not m:  # 고장난 버튼이 없는 경우
        return min(len(str(n)), res)
    # 고장난 버튼이 있는 경우
    broken = set(map(int, input().split()))
    if len(broken) == 10:  # 가능한 버튼이 없는 경우(숫자만 고장가능)
        return res
    possible = set(range(10)) - broken  # 가능한 버튼
    len_n = len(str(n))
    max_num = int(str(max(possible)) * min(6, (len_n + 1)))  # 가능한 버튼으로 만들 수 있는 최대 채널
    min_num = int(str(min(possible)) * max(1, (len_n - 1)))  # 가능한 버튼으로 만들 수 있는 최소 채널
    # 최대 채널까지 모두 눌러보는 경우
    for i in range(min_num, max_num + 1):
        for j in str(i):
            if int(j) in broken:
                break
        else:  # 고장난 버튼이 없는 경우
            # 해당 번호로 이동 후 +, - 버튼으로 이동하는 경우, 기존 res와 비교
            res = min(res, len(str(i))+abs(n-i))
    return res

print(solution())


"""
현 시점 골드 5. 제출 103997. 정답률 23.179 %
골드치고는 의외로 브루트포스. 
하지만 시간을 줄이기 위해 여러 가지치기를 해봤다.
처음에 50만까지만 순회하면 되지 않나 생각했는데
그러면 51117로 가서 내려오거나 그런 방법을 사용하지 못한다.
최댓값과 최솟값을 min, max를 이용해 구해서 순회 범위를 제한했다.
n의 길이 +-1에서 가능한 버튼으로 만들 수 있는 최대, 최소 채널.
50만 제한이니 최대 6자리까지만. 
최솟값에서 max에 1을 넣었어도 가능한 최소 버튼이 0이면 min_num이 0이 되어서 상관없다.
"""