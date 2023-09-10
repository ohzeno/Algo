# https://www.acmicpc.net/problem/14499
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
nxm 지도에 주사위가 있음.
지도의 좌표는 (r,c)로 나타냄.
주사위 전개도는 다음과 같음
    2
4   1   3
    5
    6
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여 있음.
놓인 곳 좌표는 (x,y)임. 처음에 주사위 모든 면에 0이 적혀있음
지도 각 칸에는 정수가 하나씩 쓰여 있음. 
주사위를 굴렸을 때, 
이동한 칸이 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨.
0이 아니면 칸의 숫자가 주사위의 바닥면으로 복사되며, 칸은 0이 됨.
주사위를 놓은 곳의 좌표와 이동 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여있는 값을 구하는 프로그램을 작성하라.
주사위는 지도의 바깥으로 이동시킬 수 없음. 이 경우에 해당 명령을 무시해야 하며, 출력도 하면 안됨.
명령어:  1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
이동할 때마다 윗면 출력하라.
"""

n, m, x, y, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
dice = {
    "t": 0,
    "b": 0,
    "e": 0,
    "w": 0,
    "n": 0,
    "s": 0
}

def move(cmd):
    if cmd == 1:  # 동쪽
        dice["t"], dice["e"], dice["b"], dice["w"] = dice["w"], dice["t"], dice["e"], dice["b"]
    elif cmd == 2:  # 서쪽
        dice["t"], dice["e"], dice["b"], dice["w"] = dice["e"], dice["b"], dice["w"], dice["t"]
    elif cmd == 3:  # 북쪽
        dice["t"], dice["n"], dice["b"], dice["s"] = dice["s"], dice["t"], dice["n"], dice["b"]
    elif cmd == 4:  # 남쪽
        dice["t"], dice["n"], dice["b"], dice["s"] = dice["n"], dice["b"], dice["s"], dice["t"]

for cmd in cmds:
    if cmd == 1:  # 동쪽
        if y == m - 1:  # 이미 오른쪽 끝이면 무시
            continue
        y += 1
    elif cmd == 2:
        if y == 0:
            continue
        y -= 1
    elif cmd == 3:
        if x == 0:
            continue
        x -= 1
    elif cmd == 4:
        if x == n - 1:
            continue
        x += 1
    move(cmd)
    if mat[x][y] == 0:
        mat[x][y] = dice["b"]
    else:
        dice["b"] = mat[x][y]
        mat[x][y] = 0
    print(dice["t"])


"""
현 시점 골드 4. 제출 44180. 정답률 44.259%
문제를 이해하지 못하겠다거나 까다롭다는 사람들이 많아서 풀어봤다.
문제 읽고 구현까지 15분 걸렸고 한번에 통과했다.
사람들 말과 달리 문제 묘사는 명확했다.
솔직히 골드4 치고는 지나치게 쉬웠다.
초등학교 수준의 공간지각능력이 필요한 문제.
"""
