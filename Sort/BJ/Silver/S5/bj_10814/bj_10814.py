# https://www.acmicpc.net/problem/10814
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
# 가입순서 기록 위한 i
datas = [(tuple(input().split()), i) for i in range(n)]
# 튜플로 sort하면 첫 인자로 정렬된 상태를 유지한 채로 두 번째 인자로 정렬함.
# 나이 순 정렬 후 나이 같으면 가입순.
datas.sort(key=lambda x: (int(x[0][0]), int(x[1])))
for data in datas:
    print(*data[0])
