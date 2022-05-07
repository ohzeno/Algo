# https://www.acmicpc.net/problem/1620
import sys

sys.stdin = open("input.txt")

# 포켓몬 갯수, 맞춰야하는 문제 수
# input()으로 받으니 시간초과 나서 sys.stdin.readline().rstrip()
num_pocketmon, T = map(int, sys.stdin.readline().rstrip().split())

dogam = {}
for i in range(1, num_pocketmon + 1):
    # 키: 번호, 벨류: 포켓몬
    dogam[f'{str(i)}'] = input()
# 키: 포켓몬, 벨류: 번호
# 맵으로 키, 벨류 뒤집고 dict로 다시 딕셔너리로.
reverse_dogam = dict(map(reversed, dogam.items()))

for j in range(1, T+1):
    data = sys.stdin.readline().rstrip()
    # 숫자인지 문자인지에 따라 분류할 수도 있음.
    # 2케이스 뿐이라 try except로 둘다 시도.
    try:
        print(dogam[data])
    except:
        print(reverse_dogam[data])