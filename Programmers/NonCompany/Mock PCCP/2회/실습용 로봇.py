# https://school.programmers.co.kr/learn/courses/15009/lessons/121687
"""
R: 오른쪽으로 90도 회전
L: 왼쪽으로 90도 회전
G: 전진
B: 후진
초기 위치는 0,0이고 +y축을 향하여 놓여 있다.
명령어 문자열이 주어지면 최종 위치의 x,y 좌표를 반환하라.

1 ≤ commad의 길이 ≤ 1,000,000
"""


def solution(command):
    x = y = d = 0
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for c in command:
        # match c:
        #     case "R":
        #         d = (d + 1) % 4
        #     case "L":
        #         d = (d - 1) % 4
        #     case "G":
        #         dx, dy = dirs[d]
        #         x += dx
        #         y += dy
        #     case "B":
        #         dx, dy = dirs[d]
        #         x -= dx
        #         y -= dy
        if c == "R":
            d = (d + 1) % 4
        elif c == "L":
            d = (d - 1) % 4
        else:
            dx, dy = dirs[d]
            if c == "G":
                x += dx
                y += dy
            else:
                x -= dx
                y -= dy
    return [x, y]


inputdatas = [
    ["GRGLGRG", [2, 2]],
    ["GRGRGRB", [2, 0]],
]

"""
[PCCP 모의고사 #2] 1번 - 실습용 로봇
프로그래머스 파이썬이 3.8.5라 아직 match case가 지원되지 않는다.
백준보다 늦다니...
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
