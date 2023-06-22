# https://www.acmicpc.net/problem/5781
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
큐브 정보와 회전 정보가 주어질 때 큐브가 맞춰지는지 여부를 판단하여 출력하라.
"""
from collections import deque
def rotate(mat, dir, repeat=1):
    if repeat == 0:
        return [row[:] for row in mat]
    elif repeat == 1:
        if dir == -1:
            return list(zip(*mat))[::-1]
        return list(zip(*mat[::-1]))
    elif repeat == 2:
        return [row[::-1] for row in mat][::-1]

def complete(cube):
    for mat in cube.values():
        color = mat[0][0]
        for row in mat:
            if row.count(color) != 3:
                return False
    return True

def init_cube():
    cube = {i: [] for i in range(1, 7)}
    cube[5] = [list(input().split()) for _ in range(3)]
    for i in range(3):
        datas = list(input().split())
        cube[1].append(datas[:3])
        cube[2].append(datas[3:6])
        cube[3].append(datas[6:9])
        cube[4].append(datas[9:])
    cube[6] = [list(input().split()) for _ in range(3)]
    return cube

adj_d = {
    1: [(5, -1, 1),
        (2, -1, 1),
        (6, -1, 1),
        (4, +1, 1)],
    2: [(1, +1, 1),
        (5, -1, 0),
        (3, -1, 1),
        (6, -1, 2)],
    3: [(6, +1, 1),
        (2, +1, 1),
        (5, +1, 1),
        (4, -1, 1)],
    4: [(1, -1, 1),
        (6, -1, 0),
        (3, +1, 1),
        (5, +1, 2)],
    5: [(4, +1, 2),
        (3, +1, 2),
        (2, +1, 2),
        (1, +1, 2)],
    6: [(1, -1, 0),
        (2, -1, 0),
        (3, -1, 0),
        (4, -1, 0)]
}
for _ in range(int(input())):
    cube = init_cube()
    cmds = list(map(int, input().split()))
    for cmd in cmds:
        if not cmd:
            break
        cur = abs(cmd)
        dir = 1 if cmd > 0 else -1
        tmps = {cur: rotate(cube[cur][:], dir)}
        adjs, rows = [], deque()
        for face, d, rep in adj_d[cur]:
            tmps[face] = rotate(cube[face][:], d, rep)
            adjs.append(face)
            rows.append(tmps[face][2])
        rows.rotate(dir)
        for face, row in zip(adjs, rows):
            tmps[face][2] = row
        for face, d, rep in adj_d[cur]:
            tmps[face] = rotate(tmps[face][:], -d, rep)
        cube.update(tmps)
    if complete(cube):
        print("Yes, grandpa!")
    else:
        print("No, you are wrong!")

"""
현 시점 플래 5. 제출 31. 정답률 75.862%
삼성 기출 큐빙이 생각나는 큐브문제.
이전에 삼성 기출 풀 때는 노가다로 회전시켰는데
이번엔 괜찮은 방법이 생각나서 시험해봤다.
직관적으로 작성하기 위해 인접면들을 회전시키고 
deque로 줄을 회전시킨 후 면의 방향을 되돌렸다.
시간을 조금 더 쓰고 코드를 깔끔하게 만드는 방법.
인접면들을 어떤 순서로 놓고 어떻게 회전시켜야 하는지 
생각하는 것 말고는 어렵지 않았다.
한 번에 통과했다.
삼성 기출때도 그랬지만 사람들이 노가다로 통과해서
일부러 짧게 만든게 아닌데도 내 코드가 모든 언어 숏코드 2위가 됐다...
"""