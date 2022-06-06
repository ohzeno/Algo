# https://www.acmicpc.net/problem/1181
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = [input() for _ in range(n)]
datas = list(set(datas))  # 중복 제거
# 튜플로 sort하면 첫 인자로 정렬된 상태를 유지한 채로 두 번째 인자로 정렬함.
# 길이로 정렬 후 사전순 정렬
datas.sort(key=lambda x: (len(x), x))
for data in datas:
    print(data)
