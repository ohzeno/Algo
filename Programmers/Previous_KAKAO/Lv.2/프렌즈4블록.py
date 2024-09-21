# https://school.programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    # 2x2 블럭 터짐. 모서리만 겹치는 2x2블럭 여럿이 같이 터지기도 함.
    # 주어진 board에서 최종적으로 몇 개의 블럭이 터지는지 리턴
    board = [list(row) for row in board]  # 문자열을 리스트로 바꿈.
    answer = 0
    def check(i, j):
        # 0이 아니고 4칸이 같은 문자면 True
        if board[i][j] and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
            return True
        return False

    def fall():
        for c in range(n):  # 칼럼마다 체크
            for r in range(m-1, 0, -1):  # 아래쪽 행부터
                if not board[r][c]:  # 비어있으면
                    # 바로 위칸부터 제일 위까지 비어있지 않은 칸 찾아서 아래로 떨구기.
                    for k in range(r-1, -1, -1):
                        if board[k][c]:
                            board[r][c], board[k][c] = board[k][c], board[r][c]
                            break

    while True:
        remove_set = set()  # 겹치는 좌표를 처리하기 위해 set로 좌표 기록.
        # 좌상단부터 4칸 체크.
        for c in range(n - 1):
            for r in range(m - 1):
                if check(r, c):  # 터질 좌표면 set에 추가.
                    remove_set.add((r, c))
                    remove_set.add((r+1, c))
                    remove_set.add((r, c+1))
                    remove_set.add((r+1, c+1))
        answer += len(remove_set)  # 터진 블럭 기록
        if not remove_set:  # 더 터질 것 없으면 종료.
            break
        for i, j in remove_set:  # 터진 블럭을 0으로 바꿈.
            board[i][j] = 0
        fall()  # fall작업
    return answer

inputdatas = [
    [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
    [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]],
]

"""
2018 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 18분 걸렸다.
폭발할 블럭이 겹치는 경우가 나온 문제는 처음 풀어봤으나 set를 사용하면 그리 어렵지 않았다.
"""
for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
