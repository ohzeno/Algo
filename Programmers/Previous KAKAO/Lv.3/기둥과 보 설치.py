# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# 기존 풀이. remove시 주변 좌표 안정성 체크
def solution0(n, build_frame):
    # 기둥은 바닥 위, 보의 끝부분 위, 또는 다른 기둥 위에 있어야 함.
    # 보는 한쪽 끝이 기둥 위에 있거나 양쪽 끝이 다른 보와 동시에 연결되어 있어야 함.
    # 보 설치는 왼쪽에서 오른쪽으로. 기둥은 아래에서 위로.
    # 삭제 기능 있음. 삭제 후 규칙 위반하는 명령은 무시됨.
    # build_frame의 모든 명령을 수행 후 구조물의 상태를 리턴.
    # n은 5~100   build_frame 세로 1~1000 가로 4
    # build_frame 원소 [x, y, a, b] x,y는 가로 세로 좌표.
    # a가 0이면 기둥, 1이면 보. b가 0이면 삭제, 1이면 설치
    # 구조물이 겹치도록 설치하거나 없는 구조물을 삭제하는 경우는 주어지지 않음.
    # 최종 구조물은 가로길이가 3인 2차원 배열. 원소는 [x, y, a]
    # x, y는 교차점 좌표, 가로, 세로.  a가 0이면 기둥, 1은 보
    # x좌표 기준으로 오름차순 정렬, x좌표 같으면 y좌표 기준 오름차순. x, y 좌표가 모두 같으면 기둥이 앞
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    def isok(c, r, a):
        if a == 0:  # 기둥이면
            # 바닥 위거나, 기둥 위거나
            # 보 위거나.
            if r == 0 or board[r - 1][c][0] \
                    or (c and board[r][c - 1][1]) or (c < n and board[r][c][1]):
                return True
        elif a == 1:  # 보면(바닥에 설치하는 경우 주어지지 않음)
            # 한쪽 끝이 기둥 위거나
            # 양쪽 끝이 다른 보와 연결되어 있거나
            if board[r - 1][c][0] or (c < n and board[r - 1][c + 1][0]) \
                    or (0 < c < n - 1 and board[r][c - 1][1] and board[r][c + 1][1]):
                return True
        return False

    def build(c, r, a):
        if isok(c, r, a):
            if a == 0:  # 기둥이면
                board[r][c][0] = 1
            else:  # 보면
                board[r][c][1] = 1

    def remove(c, r, a):
        if a == 0:  # 기둥이면
            board[r][c][0] = 0  # 기둥 삭제했을 때
            if board[r + 1][c][0] and not isok(c, r + 1, 0):  # 위 칸에 기둥이 있고 괜찮지 않다면
                board[r][c][0] = 1  # 기둥 다시 세우고 리턴
                return
            if c > 0 and board[r + 1][c - 1][1] and not isok(c - 1, r + 1, 1):  # 왼쪽에 보가 얹혀있고 괜찮지 않으면
                board[r][c][0] = 1
                return
            if c < n and board[r + 1][c][1] and not isok(c, r + 1, 1):  # 오른쪽에 보가 얹혀있고 괜찮지 않으면
                board[r][c][0] = 1
                return
        elif a == 1:  # 보면
            board[r][c][1] = 0  # 보 삭제했을 때
            if 0 < r < n:  # 제일 윗줄이나 바닥 아니면 기둥체크
                if board[r][c + 1][0] and not isok(c + 1, r, 0):  # 오른쪽 위에 기둥이 있고 괜찮지 않으면
                    board[r][c][1] = 1  # 보 다시 세우고 리턴
                    return
                if board[r][c][0] and not isok(c, r, 0):  # 바로 위에 기둥 있고 괜찮지 않으면
                    board[r][c][1] = 1
                    return
            if c > 0 and board[r][c - 1][1] and not isok(c - 1, r, 1):  # 왼쪽에 보 있고 괜찮지 않으면
                board[r][c][1] = 1
                return
            if board[r][c + 1][1] and not isok(c + 1, r, 1):  # 오른쪽에 보 있고 괜찮지 않으면
                board[r][c][1] = 1
                return

    for x, y, a, b in build_frame:
        if b == 1:
            build(x, y, a)
        else:
            remove(x, y, a)
    answer = []
    for r in range(n + 1):
        for c in range(n + 1):
            if board[r][c][0]:
                answer.append([c, r, 0])
            if board[r][c][1]:
                answer.append([c, r, 1])
    answer.sort()
    return answer

# 새 풀이. remove시 현재까지 설치한 모든 좌표 안정성 체크
def solution(n, build_frame):
    answer = []
    def isok(c, r, is_beam):
        if not is_beam:  # 기둥의 경우
            # 바닥이거나
            # 밑에 기둥이 있거나
            # 왼쪽에 보가 있거나
            # 현 위치에 보가 있거나
            if r == 0 \
                    or [c, r - 1, 0] in answer \
                    or [c - 1, r, 1] in answer \
                    or [c, r, 1] in answer:
                return True
        elif is_beam:  # 보의 경우
            # 밑에 기둥이 있거나
            # 오른쪽 아래에 기둥이 있거나
            # 양쪽에 보가 있거나
            if [c, r - 1, 0] in answer \
                or [c + 1, r - 1, 0] in answer \
                or (
                [c - 1, r, 1] in answer
                and [c + 1, r, 1] in answer
            ):
                return True
        return False

    def build(c, r, is_beam):
        if isok(c, r, is_beam):  # 규칙에 맞으면 추가
            answer.append([c, r, is_beam])

    def remove(c, r, is_beam):
        answer.remove([c, r, is_beam])  # 일단 제거해보고
        for c2, r2, is_beam2 in answer:  # 설치된 구조물 순회하며
            if not isok(c2, r2, is_beam2):  # 문제가 있다면
                answer.append([c, r, is_beam])  # 다시 추가하고 중단
                return

    for x, y, is_beam, is_build in build_frame:
        if is_build:  # 설치작업
            build(x, y, is_beam)
        else:  # 제거작업
            remove(x, y, is_beam)
    return sorted(answer)  # 정렬해서 리턴

inputdatas = [
    # [
    #     9, [[2, 0, 0, 1], [9, 0, 0, 1], [9, 1, 1, 1], [8, 1, 1, 1], [8, 1, 0, 1], [8, 0, 0, 1]]
    # ],
    # [4, [[1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1], [2, 1, 0, 1], [1, 2, 1, 1], [1, 1, 0, 0]]],
    # [5,
    #  [
    #      [1, 0, 0, 1],
    #      [1, 1, 1, 1],
    #      [2, 1, 0, 1],
    #      [2, 2, 1, 1],
    #      [5, 0, 0, 1],
    #      [5, 1, 0, 1],
    #      [4, 2, 1, 1],
    #      [3, 2, 1, 1],
    #  ]
    # ],
    [5,
     [
         [0, 0, 0, 1],
         [2, 0, 0, 1],
         [4, 0, 0, 1],
         [0, 1, 1, 1],
         [1, 1, 1, 1],
         [2, 1, 1, 1],
         [3, 1, 1, 1],
         [2, 0, 0, 0],
         [1, 1, 1, 0],
         [2, 2, 0, 1],
     ]
    ]
]

"""
2020 카카오 공채 기출. Lv.3.
초안은 88분 걸렸다. 오래걸린 이유 중 하나가, "구조물이 겹치도록 설치하는 경우는 주어지지 않는다"라는 말이 애매해서다.
기둥 위에 보와 기둥이 같이 올 수 있는 케이스를 생각했지만 예시에서는 없고 저런 문구가 있어서 
일단 교차점에서 기둥과 보과 겹치지 않는다고 가정하고 풀고 제출한 후에 확인해보기로 했다.
아니나 다를까 초안은 테케 6, 7만 통과했다. 
다시 보다보니 'x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.'가 있어서 기둥과 보가 겹칠 수 있다.
일부러 설명을 애매하게 하고 예외를 찾을 수 있나를 검증하는 문제같긴 한데...
보, 기둥이 겹칠 수 있을 가능성을 생각했음에도 그렇게 구현하지 않은 이유는,
보, 기둥이 겹치면 조건이 많아져 구현이 까다로워져 시간낭비가 심하기 때문이다.
결국 시간 아끼려다 시간을 더 낭비하게 됐다.
겹침을 허용하도록 32분 더 구현하였으나 테케 5, 6, 7만 통과했다. 
아무리 봐도 틀린게 없어서 다른 정답풀이와 내 풀이에 인풋값을 넣어보며 다른 경우를 찾았다.
'벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.'에 위배되는 케이스에서 내 풀이와 다른 풀이의 아웃풋이 달랐다.
다음날 풀이를 60분정도 살펴보다 오류를 찾았다. isok()의 기둥 케이스에서 현 좌표의 보를 체크해야 하는데 오른쪽 보를 체크했다... 3개 케이스랑 예시 2개 맞은게 용한 지경. 가장 기초적인 부분에서 실수를 한거라 좀 많이 당황스럽다.
다른 풀이를 보면 remove에서 나처럼 복잡하게 체크하지 않는다. build_frame의 길이가 1000, n이 100이 최대라는 점에 착안하여, 삭제 명령이 들어오면 일단 삭제 후 지금까지 설치된 좌표들을 일일이 순회하며 안정성 체크를 해주고, 문제가 있다면 복구한다. 나는 효율성체크가 없는 경우에도 시간초과를 많이 경험하여 그런 비효율적 방법을 시도하지 못했다. 하지만 구현난이도가 엄청나게 내려가므로 실제 시험에서는 그렇게 풀었어야 했을 듯 하다. 기존 풀이는 solution0으로, 해당 풀이는 solution으로 작성해놓았다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
