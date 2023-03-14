# https://www.acmicpc.net/problem/9375
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
옷 이름, 종류가 주어졌을 때 옷을 입을 수 있는 경우의 수를 구하는 문제.
알몸은 취급x. 같은 종류 옷은 하나만 입을 수 있음.
"""
for _ in range(int(input())):
    clothes = {}
    for _ in range(int(input())):
        name, type = input().split()
        # clothes[type]이 없으면 0을 벨류로.
        # 있으면 value를 cloth에 할당.
        cloth = clothes.setdefault(type, 0)
        clothes[type] = cloth + 1  # 종류 추가.
    answer = 1
    for cloth in clothes.values():  # 종류별 옷의 수.
        answer *= cloth + 1  # 안입는 경우를 위해 +1.
    print(answer - 1)  # 알몸을 제외하기 위해 -1.


"""
현 시점 실버3. 제출 28533, 정답률 54.984%
조합 변형. 종류당 하나만 입거나/입지 않는다.
clothes[type]는 해당 type의 옷의 종류 수. 안입는 경우를 위해 +1
종류별로 곱한 후에 -1을 하는 이유는 알몸을 제외하기 위함.
"""