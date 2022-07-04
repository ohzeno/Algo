# https://www.acmicpc.net/problem/11034
import sys
sys.stdin = open("input.txt")

while True:
    try:
        a, b, c = map(int, input().split())
        # 최대한 많이 움직이려면 거리가 큰 쪽으로 캥거루가 들어가야 함. 둘 사이의 거리가 n이면 n-1회 채워넣을 수 있으므로 아래와 같음.
        print(max(b-a, c-b)-1)
    except:
        break
