# https://school.programmers.co.kr/learn/courses/30/lessons/49994
"""
0,0에서 시작.
좌표평면은 -5,-5부터 5,5까지.
이동 명령을 수행하면서 캐릭터가 처음 걸어본 길의 길이를 구하라
"""


def solution(dirs):
    def move(dir):
        nonlocal x, y
        dx, dy = dir2pos[dir]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(tuple(sorted([(x, y), (nx, ny)])))
            x, y = nx, ny

    dir2pos = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    visited = set()
    x, y = 0, 0
    for dir in dirs:
        move(dir)
    return len(visited)


inputdatas = [
    "ULURRDLLU",
    "LULLLLLLU",
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.2. 현 시점 완료한 사람 10,326명, 정답률 57%
입력 변수명이 dirs인데 딕셔너리를 dirs로 선언해서 좀 헤매서 10분이 걸렸다.
더 나은 풀이가 있나 풀이들을 봤는데
베스트 풀이가 나랑 로직이 거의 같다.
"""

for t in inputdatas:
    print(solution(t))
